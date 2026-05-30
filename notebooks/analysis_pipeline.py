"""
Pipeline phân tích đầy đủ cho nghiên cứu:
"Phân tích các yếu tố ảnh hưởng đến sự hài lòng và sự khác biệt
 giữa các nhóm khách hàng tại Pizza 4P's"

Các bước:
  1. Load dữ liệu (survey + POS)
  2. Tiền xử lý
  3. Cronbach's Alpha cho từng nhân tố
  4. EFA (Exploratory Factor Analysis)
  5. Tính điểm tổng hợp 5 nhân tố và CS
  6. MLR toàn bộ + kiểm định (R², F, t, VIF)
  7. Tính RFM scores
  8. Phân khúc khách hàng (K-Means, k=4)
  9. MLR cho từng phân khúc + bảng so sánh hệ số
 10. Kết luận

Chạy:  python3 analysis_pipeline.py
Output: file kết quả lưu vào ../data/results/
"""

import os
import json
import numpy as np
import pandas as pd
from pathlib import Path

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import (
    calculate_bartlett_sphericity, calculate_kmo
)

# --------------------- CẤU HÌNH ---------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = DATA_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

ITEMS = {
    "HH": ["HH1", "HH2", "HH3", "HH4"],
    "TC": ["TC1", "TC2", "TC3", "TC4"],
    "DU": ["DU1", "DU2", "DU3", "DU4"],
    "DB": ["DB1", "DB2", "DB3", "DB4"],
    "CT": ["CT1", "CT2", "CT3"],
}
CS_ITEMS = ["CS1", "CS2", "CS3"]
ANALYSIS_DATE = pd.Timestamp("2025-12-31")


# --------------------- CÁC HÀM PHỤ ---------------------
def cronbach_alpha(df_items: pd.DataFrame) -> float:
    """Tính Cronbach's Alpha = (k/(k-1)) * (1 - Σ var_i / var_total)."""
    k = df_items.shape[1]
    item_vars = df_items.var(axis=0, ddof=1)
    total_var = df_items.sum(axis=1).var(ddof=1)
    if total_var == 0:
        return float("nan")
    alpha = (k / (k - 1)) * (1 - item_vars.sum() / total_var)
    return float(alpha)


def item_total_correlation(df_items: pd.DataFrame) -> pd.Series:
    """Hệ số tương quan biến – tổng (item-total correlation, đã trừ chính item đó)."""
    out = {}
    for col in df_items.columns:
        rest = df_items.drop(columns=[col]).sum(axis=1)
        out[col] = df_items[col].corr(rest)
    return pd.Series(out)


def vif_table(X: pd.DataFrame) -> pd.DataFrame:
    """
    Bảng VIF cho mỗi biến.
    Lưu ý: phải thêm constant vào X trước khi tính VIF, nếu không
    statsmodels sẽ tính sai (cho ra giá trị quá cao).
    """
    Xc = sm.add_constant(X)
    rows = []
    for i, col in enumerate(Xc.columns):
        if col == "const":
            continue
        v = variance_inflation_factor(Xc.values, i)
        rows.append({"variable": col, "VIF": round(v, 3)})
    return pd.DataFrame(rows)


def fmt(x, n=4):
    return round(float(x), n) if pd.notna(x) else x


# --------------------- BƯỚC 1: LOAD DATA ---------------------
print("=" * 70)
print("BƯỚC 1: LOAD DỮ LIỆU")
print("=" * 70)

survey = pd.read_csv(DATA_DIR / "survey_servqual.csv")
pos = pd.read_csv(DATA_DIR / "pos_transactions.csv", parse_dates=["transaction_date"])
print(f"Survey:  {survey.shape[0]} customers × {survey.shape[1]} cols")
print(f"POS:     {pos.shape[0]} transactions × {pos.shape[1]} cols")


# --------------------- BƯỚC 2: TIỀN XỬ LÝ ---------------------
print("\n" + "=" * 70)
print("BƯỚC 2: TIỀN XỬ LÝ")
print("=" * 70)

# 2a) Kiểm tra missing
miss_survey = survey.isna().sum().sum()
miss_pos = pos.isna().sum().sum()
print(f"Missing values - Survey: {miss_survey} | POS: {miss_pos}")

# 2b) Kiểm tra outliers Likert (phải nằm trong [1, 5])
all_likert_items = sum(ITEMS.values(), []) + CS_ITEMS
outliers = ((survey[all_likert_items] < 1) | (survey[all_likert_items] > 5)).sum().sum()
print(f"Outliers ngoài thang Likert 1-5: {outliers}")

# 2c) Tích hợp data: chỉ giữ customer có cả survey + POS
common_ids = set(survey["customer_id"]) & set(pos["customer_id"])
survey = survey[survey["customer_id"].isin(common_ids)].reset_index(drop=True)
pos = pos[pos["customer_id"].isin(common_ids)].reset_index(drop=True)
print(f"Sau tích hợp: {survey.shape[0]} customers (có đầy đủ survey + POS)")


# --------------------- BƯỚC 3: CRONBACH'S ALPHA ---------------------
print("\n" + "=" * 70)
print("BƯỚC 3: KIỂM ĐỊNH ĐỘ TIN CẬY THANG ĐO (Cronbach's Alpha)")
print("=" * 70)

cronbach_results = []
for factor, items in ITEMS.items():
    sub = survey[items]
    alpha = cronbach_alpha(sub)
    itc = item_total_correlation(sub)
    print(f"\n[{factor}] α = {alpha:.4f}  (yêu cầu ≥ 0.6)  | n_items = {len(items)}")
    print(f"   Item-total correlation:")
    for item, r in itc.items():
        flag = "✓" if r >= 0.3 else "✗"
        print(f"     {flag} {item}: {r:.4f}")
    cronbach_results.append({"factor": factor, "alpha": fmt(alpha), "n_items": len(items)})

# CS scale
cs_alpha = cronbach_alpha(survey[CS_ITEMS])
cronbach_results.append({"factor": "CS", "alpha": fmt(cs_alpha), "n_items": len(CS_ITEMS)})
print(f"\n[CS] α = {cs_alpha:.4f}")

cronbach_df = pd.DataFrame(cronbach_results)
cronbach_df.to_csv(RESULTS_DIR / "01_cronbach_alpha.csv", index=False)


# --------------------- BƯỚC 4: EFA ---------------------
print("\n" + "=" * 70)
print("BƯỚC 4: PHÂN TÍCH NHÂN TỐ KHÁM PHÁ (EFA)")
print("=" * 70)

efa_items = sum(ITEMS.values(), [])  # chỉ dùng các biến quan sát SERVQUAL
X_efa = survey[efa_items].astype(float)

# 4a) KMO + Bartlett
chi_square, p_bartlett = calculate_bartlett_sphericity(X_efa)
kmo_per_var, kmo_overall = calculate_kmo(X_efa)
print(f"KMO overall = {kmo_overall:.4f}  (yêu cầu ≥ 0.5)")
print(f"Bartlett's test: χ² = {chi_square:.2f}, p-value = {p_bartlett:.6f}  (yêu cầu p < 0.05)")

# 4b) Chạy EFA với 5 nhân tố, varimax rotation
fa = FactorAnalyzer(n_factors=5, rotation="varimax", method="principal")
fa.fit(X_efa)
loadings = pd.DataFrame(
    fa.loadings_,
    index=efa_items,
    columns=[f"F{i+1}" for i in range(5)],
)
print("\nFactor loadings (đã làm tròn 3 chữ số, |loading| ≥ 0.4 in đậm):")
print(loadings.round(3).to_string())

# Eigenvalues + variance explained
ev_orig, ev_common = fa.get_eigenvalues()
var_exp = fa.get_factor_variance()
ve_df = pd.DataFrame({
    "factor": [f"F{i+1}" for i in range(5)],
    "eigenvalue": [round(v, 3) for v in ev_orig[:5]],
    "var_explained": [round(v, 3) for v in var_exp[1]],
    "cum_var_explained": [round(v, 3) for v in var_exp[2]],
})
print("\nEigenvalues + Variance explained:")
print(ve_df.to_string(index=False))

loadings.to_csv(RESULTS_DIR / "02_efa_loadings.csv")
ve_df.to_csv(RESULTS_DIR / "02_efa_variance.csv", index=False)


# --------------------- BƯỚC 5: TÍNH ĐIỂM TỔNG HỢP ---------------------
print("\n" + "=" * 70)
print("BƯỚC 5: TÍNH ĐIỂM TỔNG HỢP 5 NHÂN TỐ + CS")
print("=" * 70)

scores = pd.DataFrame({"customer_id": survey["customer_id"]})
for factor, items in ITEMS.items():
    scores[factor] = survey[items].mean(axis=1)
scores["CS"] = survey[CS_ITEMS].mean(axis=1)

print(scores[["HH", "TC", "DU", "DB", "CT", "CS"]].describe().round(3))


# --------------------- BƯỚC 6: HỒI QUY TỔNG ---------------------
print("\n" + "=" * 70)
print("BƯỚC 6: HỒI QUY TUYẾN TÍNH ĐA BIẾN — TOÀN BỘ MẪU")
print("=" * 70)

X = scores[["HH", "TC", "DU", "DB", "CT"]]
y = scores["CS"]
X_const = sm.add_constant(X)
model_overall = sm.OLS(y, X_const).fit()
print(model_overall.summary())

print("\nVIF:")
vif = vif_table(X)
print(vif.to_string(index=False))

# Lưu
overall_coef = pd.DataFrame({
    "variable": model_overall.params.index,
    "coef": model_overall.params.values.round(4),
    "std_err": model_overall.bse.values.round(4),
    "t": model_overall.tvalues.values.round(4),
    "p_value": model_overall.pvalues.values.round(4),
})
overall_coef.to_csv(RESULTS_DIR / "03_mlr_overall.csv", index=False)
vif.to_csv(RESULTS_DIR / "03_mlr_overall_vif.csv", index=False)


# --------------------- BƯỚC 7: TÍNH RFM ---------------------
print("\n" + "=" * 70)
print("BƯỚC 7: TÍNH ĐIỂM RFM TỪ POS")
print("=" * 70)

# Recency (ngày kể từ giao dịch gần nhất)
last_tx = pos.groupby("customer_id")["transaction_date"].max().rename("last_tx")
recency = (ANALYSIS_DATE - last_tx).dt.days.rename("R")

# Frequency
frequency = pos.groupby("customer_id").size().rename("F")

# Monetary
monetary = pos.groupby("customer_id")["amount_vnd"].sum().rename("M")

rfm = pd.concat([recency, frequency, monetary], axis=1).reset_index()
print(rfm.describe().round(2))


# --------------------- BƯỚC 8: PHÂN KHÚC RFM (K-MEANS) ---------------------
print("\n" + "=" * 70)
print("BƯỚC 8: PHÂN KHÚC KHÁCH HÀNG (K-Means trên RFM scaled)")
print("=" * 70)

# Chuẩn hóa: log transform M (skewed), rồi z-score
rfm_scaled = rfm.copy()
rfm_scaled["M_log"] = np.log1p(rfm_scaled["M"])
features = ["R", "F", "M_log"]
scaler = StandardScaler()
X_rfm = scaler.fit_transform(rfm_scaled[features])

# Chọn k = 4 (theo proposal)
K_RANGE = range(2, 8)
sil_scores = {}
for k in K_RANGE:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    lab = km.fit_predict(X_rfm)
    sil_scores[k] = silhouette_score(X_rfm, lab)
print("Silhouette scores theo k:")
for k, s in sil_scores.items():
    print(f"  k={k}: {s:.4f}")

K = 4
km = KMeans(n_clusters=K, random_state=42, n_init=10)
rfm["cluster_id"] = km.fit_predict(X_rfm)

# Đặt tên cluster theo profile (R thấp+F cao+M cao = VIP, ...)
profile = rfm.groupby("cluster_id")[["R", "F", "M"]].mean().round(0)
print("\nProfile mỗi cluster (mean):")
print(profile)

# Sắp xếp tên theo M giảm dần và R tăng dần
profile_sorted = profile.copy()
profile_sorted["score"] = profile_sorted["F"] + profile_sorted["M"] / 1_000_000 - profile_sorted["R"] / 30
order = profile_sorted["score"].sort_values(ascending=False).index.tolist()
labels = ["VIP", "Loyal", "Potential", "AtRisk"]
cluster_name_map = dict(zip(order, labels))
rfm["segment"] = rfm["cluster_id"].map(cluster_name_map)
print("\nÁnh xạ cluster_id → segment name:")
print(cluster_name_map)
print("\nPhân bố segment:")
print(rfm["segment"].value_counts(normalize=True).round(3))

rfm.to_csv(RESULTS_DIR / "04_rfm_segmented.csv", index=False)


# --------------------- BƯỚC 9: HỒI QUY THEO TỪNG PHÂN KHÚC ---------------------
print("\n" + "=" * 70)
print("BƯỚC 9: HỒI QUY THEO TỪNG PHÂN KHÚC")
print("=" * 70)

merged = scores.merge(rfm[["customer_id", "segment"]], on="customer_id")

per_segment_results = []
for seg in ["VIP", "Loyal", "Potential", "AtRisk"]:
    sub = merged[merged["segment"] == seg]
    if len(sub) < 20:
        print(f"\n[{seg}] n={len(sub)} — quá ít, bỏ qua")
        continue
    Xs = sub[["HH", "TC", "DU", "DB", "CT"]]
    ys = sub["CS"]
    Xs_c = sm.add_constant(Xs)
    m = sm.OLS(ys, Xs_c).fit()
    print(f"\n[{seg}] n={len(sub)} | R² = {m.rsquared:.4f} | adj R² = {m.rsquared_adj:.4f}")
    coef_row = {"segment": seg, "n": len(sub), "R2": fmt(m.rsquared), "adj_R2": fmt(m.rsquared_adj)}
    for var in ["const", "HH", "TC", "DU", "DB", "CT"]:
        coef_row[f"{var}_coef"] = fmt(m.params[var])
        coef_row[f"{var}_p"] = fmt(m.pvalues[var])
    per_segment_results.append(coef_row)

per_seg_df = pd.DataFrame(per_segment_results)
per_seg_df.to_csv(RESULTS_DIR / "05_mlr_per_segment.csv", index=False)
print("\n--- BẢNG SO SÁNH HỆ SỐ HỒI QUY GIỮA CÁC PHÂN KHÚC ---")
print(per_seg_df.to_string(index=False))


# --------------------- BƯỚC 10: TÓM TẮT ---------------------
print("\n" + "=" * 70)
print("BƯỚC 10: TÓM TẮT KẾT LUẬN")
print("=" * 70)

# Yếu tố ảnh hưởng mạnh nhất theo từng phân khúc
print("\nYếu tố có hệ số β cao nhất (significant, p<0.05) theo phân khúc:")
for _, r in per_seg_df.iterrows():
    seg = r["segment"]
    factor_betas = {
        f: (r[f"{f}_coef"], r[f"{f}_p"]) for f in ["HH", "TC", "DU", "DB", "CT"]
    }
    sig = {f: b for f, (b, p) in factor_betas.items() if p < 0.05}
    if sig:
        top = max(sig.items(), key=lambda kv: kv[1])
        print(f"  • {seg}: yếu tố {top[0]} (β = {top[1]})")

summary = {
    "n_customers": int(len(survey)),
    "n_transactions": int(len(pos)),
    "cronbach_alpha": cronbach_df.set_index("factor")["alpha"].to_dict(),
    "kmo": fmt(kmo_overall),
    "bartlett_p": fmt(p_bartlett, 6),
    "overall_R2": fmt(model_overall.rsquared),
    "overall_adj_R2": fmt(model_overall.rsquared_adj),
    "overall_coef": {
        v: fmt(model_overall.params[v]) for v in ["const", "HH", "TC", "DU", "DB", "CT"]
    },
    "segments_distribution": rfm["segment"].value_counts().to_dict(),
}
with open(RESULTS_DIR / "00_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print(f"\n✓ Tất cả kết quả lưu tại: {RESULTS_DIR}")
print("✓ Pipeline hoàn tất.")
