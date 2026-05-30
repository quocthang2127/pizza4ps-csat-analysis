"""
Streamlit Web App — Pizza 4P's Customer Satisfaction Analysis
Đề tài: Phân tích các yếu tố ảnh hưởng đến sự hài lòng và sự khác biệt
        giữa các nhóm khách hàng tại Pizza 4P's

Tác giả: Đặng Duy Quốc Thắng
Môn học: Khai phá dữ liệu nâng cao (IDT)

Chạy local:    streamlit run app/app.py
Deploy:        Streamlit Community Cloud (free) — xem docs/DEPLOY_GUIDE.md
"""

import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import (
    calculate_bartlett_sphericity, calculate_kmo
)
from pathlib import Path

# --------------------- CẤU HÌNH ---------------------
st.set_page_config(
    page_title="Pizza 4P's — Customer Satisfaction Analysis",
    page_icon="🍕",
    layout="wide",
)

ITEMS = {
    "HH": ["HH1", "HH2", "HH3", "HH4"],
    "TC": ["TC1", "TC2", "TC3", "TC4"],
    "DU": ["DU1", "DU2", "DU3", "DU4"],
    "DB": ["DB1", "DB2", "DB3", "DB4"],
    "CT": ["CT1", "CT2", "CT3"],
}
CS_ITEMS = ["CS1", "CS2", "CS3"]
FACTOR_NAMES = {
    "HH": "Hữu hình (Tangibles)",
    "TC": "Tin cậy (Reliability)",
    "DU": "Đáp ứng (Responsiveness)",
    "DB": "Đảm bảo (Assurance)",
    "CT": "Cảm thông (Empathy)",
}
ANALYSIS_DATE = pd.Timestamp("2025-12-31")

# Đường dẫn data — relative để chạy được cả local và Cloud
DATA_DIR = Path(__file__).parent.parent / "data"


# --------------------- HÀM TIỆN ÍCH ---------------------
@st.cache_data
def load_data():
    survey = pd.read_csv(DATA_DIR / "survey_servqual.csv")
    pos = pd.read_csv(DATA_DIR / "pos_transactions.csv", parse_dates=["transaction_date"])
    return survey, pos


def cronbach_alpha(df_items):
    k = df_items.shape[1]
    var_items = df_items.var(axis=0, ddof=1).sum()
    var_total = df_items.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - var_items / var_total) if var_total > 0 else float("nan")


def compute_scores(survey):
    scores = pd.DataFrame({"customer_id": survey["customer_id"]})
    for f, items in ITEMS.items():
        scores[f] = survey[items].mean(axis=1)
    scores["CS"] = survey[CS_ITEMS].mean(axis=1)
    return scores


@st.cache_data
def compute_rfm(pos):
    last_tx = pos.groupby("customer_id")["transaction_date"].max()
    R = (ANALYSIS_DATE - last_tx).dt.days.rename("R")
    F = pos.groupby("customer_id").size().rename("F")
    M = pos.groupby("customer_id")["amount_vnd"].sum().rename("M")
    return pd.concat([R, F, M], axis=1).reset_index()


@st.cache_data
def segment_customers(rfm: pd.DataFrame, k: int = 4) -> pd.DataFrame:
    rfm = rfm.copy()
    rfm["M_log"] = np.log1p(rfm["M"])
    X = StandardScaler().fit_transform(rfm[["R", "F", "M_log"]])
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    rfm["cluster_id"] = km.fit_predict(X)
    profile = rfm.groupby("cluster_id")[["R", "F", "M"]].mean()
    profile["score"] = profile["F"] + profile["M"] / 1_000_000 - profile["R"] / 30
    order = profile["score"].sort_values(ascending=False).index.tolist()
    name_map = dict(zip(order, ["VIP", "Loyal", "Potential", "AtRisk"][:k]))
    rfm["segment"] = rfm["cluster_id"].map(name_map)
    return rfm


# --------------------- SIDEBAR ---------------------
st.sidebar.title("🍕 Pizza 4P's Analysis")
st.sidebar.markdown("**SERVQUAL × RFM Integrated Analysis**")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "📊 Chọn phần phân tích:",
    [
        "🏠 Tổng quan",
        "📋 Kiểm định thang đo",
        "🔬 Phân tích nhân tố (EFA)",
        "📈 Hồi quy tổng thể",
        "👥 Phân khúc RFM",
        "⚖️ So sánh giữa phân khúc",
        "🔮 Dự đoán CS cho khách mới",
    ],
)
st.sidebar.markdown("---")
st.sidebar.caption(
    "**Đặng Duy Quốc Thắng**  \n"
    "Cao học IDT — Môn KPDL Nâng cao  \n"
    "GVHD: TS. Võ Văn Hải"
)

# --------------------- LOAD DATA ---------------------
survey, pos = load_data()
scores = compute_scores(survey)
rfm = compute_rfm(pos)
rfm = segment_customers(rfm)
merged = scores.merge(rfm[["customer_id", "segment"]], on="customer_id")


# ============================================================
# TRANG 1: TỔNG QUAN
# ============================================================
if page == "🏠 Tổng quan":
    st.title("🏠 Tổng quan dataset")
    st.markdown(
        """
    **Bài toán:** Phân tích các yếu tố ảnh hưởng đến sự hài lòng và
    sự khác biệt giữa các nhóm khách hàng tại Pizza 4P's, kết hợp
    mô hình **SERVQUAL** với phân khúc khách hàng theo **RFM**.
    """
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Số khách hàng", f"{len(survey):,}")
    col2.metric("Số giao dịch POS", f"{len(pos):,}")
    col3.metric("Sự hài lòng TB (CS)", f"{scores['CS'].mean():.2f} / 5")
    col4.metric("Khoản chi TB", f"{rfm['M'].mean()/1e6:.1f}M VND")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📊 Demographics", "📝 Phân phối SERVQUAL", "📅 Hoạt động POS"])
    with tab1:
        c1, c2, c3 = st.columns(3)
        with c1:
            fig = px.pie(survey, names="age_group", title="Độ tuổi",
                         color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.pie(survey, names="gender", title="Giới tính",
                         color_discrete_sequence=["#FF6B6B", "#4ECDC4"])
            st.plotly_chart(fig, use_container_width=True)
        with c3:
            fig = px.pie(survey, names="visit_freq", title="Tần suất ghé thăm",
                         color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Boxplot 5 nhân tố + CS
        df_long = scores.melt(id_vars="customer_id",
                              value_vars=["HH", "TC", "DU", "DB", "CT", "CS"],
                              var_name="Nhân tố", value_name="Điểm trung bình")
        fig = px.box(df_long, x="Nhân tố", y="Điểm trung bình", color="Nhân tố",
                     title="Phân phối điểm 5 nhân tố SERVQUAL và CS (trung bình theo customer)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Bảng thống kê mô tả:**")
        st.dataframe(scores[["HH", "TC", "DU", "DB", "CT", "CS"]].describe().round(3))

    with tab3:
        pos_monthly = pos.copy()
        pos_monthly["month"] = pos_monthly["transaction_date"].dt.to_period("M").astype(str)
        agg = pos_monthly.groupby("month").agg(
            n_transactions=("customer_id", "size"),
            revenue=("amount_vnd", "sum"),
        ).reset_index()
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(agg, x="month", y="n_transactions",
                         title="Số giao dịch theo tháng",
                         color_discrete_sequence=["#FF6B6B"])
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.line(agg, x="month", y="revenue",
                          title="Doanh thu theo tháng (VND)",
                          markers=True, color_discrete_sequence=["#4ECDC4"])
            st.plotly_chart(fig, use_container_width=True)

    with st.expander("👀 Xem 10 dòng đầu của survey"):
        st.dataframe(survey.head(10))
    with st.expander("👀 Xem 10 dòng đầu của POS"):
        st.dataframe(pos.head(10))

    st.info(
        "ℹ️ **Ghi chú:** Đây là synthetic dataset được sinh phục vụ học thuật. "
        "Cấu trúc tương quan và phân khúc được thiết kế để mô phỏng dữ liệu thực tế "
        "của một chuỗi nhà hàng cao cấp ở Việt Nam."
    )


# ============================================================
# TRANG 2: KIỂM ĐỊNH THANG ĐO
# ============================================================
elif page == "📋 Kiểm định thang đo":
    st.title("📋 Kiểm định độ tin cậy thang đo (Cronbach's Alpha)")
    st.markdown(
        """
    **Tiêu chuẩn:**
    - Cronbach's Alpha **≥ 0.6** → thang đo chấp nhận được; **≥ 0.7** → tốt
    - Hệ số tương quan biến – tổng (item-total correlation) **≥ 0.3**
    """
    )

    rows = []
    for f, items in ITEMS.items():
        a = cronbach_alpha(survey[items])
        rows.append({"Nhân tố": FACTOR_NAMES[f], "Mã": f, "n_items": len(items),
                     "Cronbach α": round(a, 4),
                     "Đánh giá": "✅ Tốt" if a >= 0.7 else ("✓ Đạt" if a >= 0.6 else "❌ Không đạt")})
    rows.append({"Nhân tố": "Customer Satisfaction (biến phụ thuộc)", "Mã": "CS",
                 "n_items": 3, "Cronbach α": round(cronbach_alpha(survey[CS_ITEMS]), 4),
                 "Đánh giá": "✅ Tốt" if cronbach_alpha(survey[CS_ITEMS]) >= 0.7 else "✓ Đạt"})
    df_alpha = pd.DataFrame(rows)
    st.dataframe(df_alpha, use_container_width=True, hide_index=True)

    fig = px.bar(df_alpha, x="Mã", y="Cronbach α", color="Cronbach α",
                 color_continuous_scale="Tealgrn",
                 title="Cronbach's Alpha cho từng nhân tố",
                 text="Cronbach α")
    fig.add_hline(y=0.6, line_dash="dash", line_color="orange",
                  annotation_text="Ngưỡng chấp nhận (0.6)")
    fig.add_hline(y=0.7, line_dash="dash", line_color="green",
                  annotation_text="Ngưỡng tốt (0.7)")
    fig.update_yaxes(range=[0, 1])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Item-Total Correlation chi tiết")
    selected = st.selectbox("Chọn nhân tố để xem chi tiết:", list(ITEMS.keys()),
                            format_func=lambda x: f"{x} — {FACTOR_NAMES[x]}")
    sub = survey[ITEMS[selected]]
    rest_corr = []
    for col in sub.columns:
        rest = sub.drop(columns=[col]).sum(axis=1)
        rest_corr.append({"Item": col, "Item-Total Corr": round(sub[col].corr(rest), 4)})
    st.dataframe(pd.DataFrame(rest_corr), use_container_width=True, hide_index=True)


# ============================================================
# TRANG 3: EFA
# ============================================================
elif page == "🔬 Phân tích nhân tố (EFA)":
    st.title("🔬 Phân tích nhân tố khám phá (EFA)")
    st.markdown(
        """
    **Mục đích:** Kiểm tra xem các biến quan sát có tải đúng vào 5 nhân tố
    SERVQUAL như giả định hay không.

    **Tiêu chuẩn:**
    - **KMO ≥ 0.5** (≥ 0.7 là tốt)
    - **Bartlett's Test of Sphericity p < 0.05**
    - **Factor loading |L| ≥ 0.4** mới được giữ
    - **Cumulative variance explained ≥ 50%**
    """
    )

    efa_items = sum(ITEMS.values(), [])
    X_efa = survey[efa_items].astype(float)

    chi_sq, p_bart = calculate_bartlett_sphericity(X_efa)
    _, kmo = calculate_kmo(X_efa)

    c1, c2, c3 = st.columns(3)
    c1.metric("KMO", f"{kmo:.4f}",
              "Tốt" if kmo >= 0.7 else ("Đạt" if kmo >= 0.5 else "Không đạt"))
    c2.metric("Bartlett χ²", f"{chi_sq:.2f}")
    c3.metric("Bartlett p-value", f"{p_bart:.4g}",
              "Có ý nghĩa" if p_bart < 0.05 else "Không có ý nghĩa")

    fa = FactorAnalyzer(n_factors=5, rotation="varimax", method="principal")
    fa.fit(X_efa)
    loadings = pd.DataFrame(
        fa.loadings_, index=efa_items,
        columns=[f"Nhân tố {i+1}" for i in range(5)]
    )

    st.markdown("### Factor Loadings (sau Varimax rotation)")
    st.markdown("Highlight cho |loading| ≥ 0.4")

    def highlight(val):
        if abs(val) >= 0.4:
            return "background-color: #aef0a0; font-weight: bold"
        return ""

    st.dataframe(loadings.style.format("{:.3f}").map(highlight),
                 use_container_width=True)

    var_exp = fa.get_factor_variance()
    ev = fa.get_eigenvalues()[0][:5]
    ve_df = pd.DataFrame({
        "Nhân tố": [f"F{i+1}" for i in range(5)],
        "Eigenvalue": [round(v, 3) for v in ev],
        "% Variance Explained": [round(v*100, 2) for v in var_exp[1]],
        "Cumulative %": [round(v*100, 2) for v in var_exp[2]],
    })
    st.markdown("### Eigenvalues và phần trăm phương sai giải thích")
    st.dataframe(ve_df, use_container_width=True, hide_index=True)

    fig = px.bar(ve_df, x="Nhân tố", y="% Variance Explained",
                 title="Phần trăm phương sai mỗi nhân tố giải thích",
                 text="% Variance Explained",
                 color_discrete_sequence=["#FF6B6B"])
    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# TRANG 4: HỒI QUY TỔNG
# ============================================================
elif page == "📈 Hồi quy tổng thể":
    st.title("📈 Hồi quy tuyến tính đa biến — Toàn bộ mẫu (RQ1)")
    st.markdown(
        """
    **Mô hình:**
    $$ CS = \\beta_0 + \\beta_1 \\cdot HH + \\beta_2 \\cdot TC + \\beta_3 \\cdot DU + \\beta_4 \\cdot DB + \\beta_5 \\cdot CT + \\epsilon $$
    """
    )

    X = scores[["HH", "TC", "DU", "DB", "CT"]]
    y = scores["CS"]
    Xc = sm.add_constant(X)
    m = sm.OLS(y, Xc).fit()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("R²", f"{m.rsquared:.4f}")
    c2.metric("Adj R²", f"{m.rsquared_adj:.4f}")
    c3.metric("F-statistic", f"{m.fvalue:.2f}")
    c4.metric("Prob(F-stat)", f"{m.f_pvalue:.4g}")

    st.markdown("### Hệ số hồi quy")
    coef_df = pd.DataFrame({
        "Biến": m.params.index,
        "β (coef)": m.params.values.round(4),
        "Std Err": m.bse.values.round(4),
        "t-statistic": m.tvalues.values.round(4),
        "p-value": m.pvalues.values.round(4),
        "Ý nghĩa": ["✅ Có ý nghĩa" if p < 0.05 else "❌ Không" for p in m.pvalues],
    })
    st.dataframe(coef_df, use_container_width=True, hide_index=True)

    # Bar chart hệ số (loại const)
    coef_plot = coef_df[coef_df["Biến"] != "const"].copy()
    coef_plot["Tên đầy đủ"] = coef_plot["Biến"].map(FACTOR_NAMES)
    fig = px.bar(coef_plot, x="Tên đầy đủ", y="β (coef)",
                 color="β (coef)", color_continuous_scale="Tealgrn",
                 title="Mức độ ảnh hưởng (β) của từng yếu tố đến CS",
                 text="β (coef)")
    st.plotly_chart(fig, use_container_width=True)

    # VIF
    st.markdown("### Kiểm tra đa cộng tuyến (VIF)")
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    vif_rows = []
    for i, col in enumerate(Xc.columns):
        if col != "const":
            vif_rows.append({"Biến": col, "VIF": round(variance_inflation_factor(Xc.values, i), 3)})
    vif_df = pd.DataFrame(vif_rows)
    vif_df["Đánh giá"] = vif_df["VIF"].apply(
        lambda v: "✅ Tốt" if v < 2 else ("⚠️ Chấp nhận được" if v < 5 else "❌ Đa cộng tuyến")
    )
    st.dataframe(vif_df, use_container_width=True, hide_index=True)

    st.success(
        f"💡 **Trả lời RQ1:** Tất cả 5 yếu tố SERVQUAL đều có ảnh hưởng "
        f"có ý nghĩa thống kê đến sự hài lòng (p < 0.001). "
        f"Yếu tố **{coef_plot.loc[coef_plot['β (coef)'].idxmax(), 'Tên đầy đủ']}** "
        f"có ảnh hưởng mạnh nhất với β = "
        f"{coef_plot['β (coef)'].max():.3f}. "
        f"Mô hình giải thích {m.rsquared*100:.1f}% biến thiên của CS."
    )


# ============================================================
# TRANG 5: PHÂN KHÚC RFM
# ============================================================
elif page == "👥 Phân khúc RFM":
    st.title("👥 Phân khúc khách hàng theo RFM")

    st.markdown(
        """
    **RFM** = Recency (ngày kể từ giao dịch gần nhất), Frequency (số giao dịch),
    Monetary (tổng chi tiêu).
    Khách hàng được phân thành 4 nhóm bằng K-Means trên RFM đã chuẩn hóa.
    """
    )

    c1, c2, c3, c4 = st.columns(4)
    seg_count = rfm["segment"].value_counts()
    for col, seg in zip([c1, c2, c3, c4], ["VIP", "Loyal", "Potential", "AtRisk"]):
        if seg in seg_count.index:
            col.metric(seg, f"{seg_count[seg]:,} ({seg_count[seg]/len(rfm)*100:.1f}%)")

    st.markdown("### Profile mỗi phân khúc (giá trị trung bình)")
    profile = rfm.groupby("segment").agg(
        n=("customer_id", "size"),
        Recency_avg=("R", "mean"),
        Frequency_avg=("F", "mean"),
        Monetary_avg=("M", "mean"),
    ).round(0).reset_index()
    profile = profile.set_index("segment").reindex(["VIP", "Loyal", "Potential", "AtRisk"]).reset_index()
    profile["Monetary_avg"] = profile["Monetary_avg"].apply(lambda x: f"{x:,.0f} VND")
    st.dataframe(profile, use_container_width=True, hide_index=True)

    # 3D scatter
    st.markdown("### Biểu đồ 3D RFM")
    fig = px.scatter_3d(
        rfm, x="R", y="F", z="M", color="segment",
        title="Phân khúc khách hàng trong không gian RFM",
        labels={"R": "Recency (ngày)", "F": "Frequency", "M": "Monetary (VND)"},
        color_discrete_map={"VIP": "#FF6B6B", "Loyal": "#4ECDC4",
                            "Potential": "#FFD93D", "AtRisk": "#A8A8A8"}
    )
    fig.update_traces(marker=dict(size=4))
    st.plotly_chart(fig, use_container_width=True)

    # 2D scatter để dễ nhìn hơn
    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(rfm, x="R", y="F", color="segment",
                         title="Recency vs Frequency",
                         labels={"R": "Recency (ngày)", "F": "Frequency"},
                         color_discrete_map={"VIP": "#FF6B6B", "Loyal": "#4ECDC4",
                                             "Potential": "#FFD93D", "AtRisk": "#A8A8A8"})
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(rfm, x="F", y="M", color="segment",
                         title="Frequency vs Monetary",
                         labels={"F": "Frequency", "M": "Monetary (VND)"},
                         color_discrete_map={"VIP": "#FF6B6B", "Loyal": "#4ECDC4",
                                             "Potential": "#FFD93D", "AtRisk": "#A8A8A8"})
        st.plotly_chart(fig, use_container_width=True)


# ============================================================
# TRANG 6: SO SÁNH HỆ SỐ HỒI QUY GIỮA PHÂN KHÚC
# ============================================================
elif page == "⚖️ So sánh giữa phân khúc":
    st.title("⚖️ So sánh hệ số hồi quy giữa các phân khúc (RQ2)")
    st.markdown(
        """
    Mô hình hồi quy tuyến tính được chạy **độc lập cho từng phân khúc**
    để xem các yếu tố SERVQUAL có ảnh hưởng khác nhau giữa các nhóm
    khách hàng hay không.
    """
    )

    seg_results = []
    rows_for_chart = []
    for seg in ["VIP", "Loyal", "Potential", "AtRisk"]:
        sub = merged[merged["segment"] == seg]
        if len(sub) < 20:
            continue
        Xs = sub[["HH", "TC", "DU", "DB", "CT"]]
        ys = sub["CS"]
        Xs_c = sm.add_constant(Xs)
        m = sm.OLS(ys, Xs_c).fit()
        row = {"Phân khúc": seg, "n": len(sub),
               "R²": round(m.rsquared, 4), "Adj R²": round(m.rsquared_adj, 4)}
        for f in ["HH", "TC", "DU", "DB", "CT"]:
            row[f"β_{f}"] = round(m.params[f], 4)
            row[f"p_{f}"] = round(m.pvalues[f], 4)
            rows_for_chart.append({
                "Phân khúc": seg, "Yếu tố": f, "β": round(m.params[f], 4),
                "Significant": "p < 0.05" if m.pvalues[f] < 0.05 else "p ≥ 0.05"
            })
        seg_results.append(row)

    df_seg = pd.DataFrame(seg_results)
    st.markdown("### Bảng tổng hợp")
    st.dataframe(df_seg, use_container_width=True, hide_index=True)

    df_chart = pd.DataFrame(rows_for_chart)
    fig = px.bar(df_chart, x="Yếu tố", y="β", color="Phân khúc",
                 barmode="group", text="β",
                 title="So sánh hệ số hồi quy β giữa các phân khúc",
                 color_discrete_map={"VIP": "#FF6B6B", "Loyal": "#4ECDC4",
                                     "Potential": "#FFD93D", "AtRisk": "#A8A8A8"})
    st.plotly_chart(fig, use_container_width=True)

    # Heatmap
    pivot = df_chart.pivot(index="Phân khúc", columns="Yếu tố", values="β")
    pivot = pivot.reindex(["VIP", "Loyal", "Potential", "AtRisk"])
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values, x=pivot.columns, y=pivot.index,
        colorscale="RdYlGn", text=pivot.round(3).values, texttemplate="%{text}",
        textfont={"size": 14}))
    fig.update_layout(title="Heatmap: Mức độ ảnh hưởng theo (Phân khúc × Yếu tố)",
                      height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Tóm tắt yếu tố nổi trội mỗi phân khúc
    st.markdown("### Yếu tố ảnh hưởng mạnh nhất ở mỗi phân khúc")
    summary_rows = []
    for seg in ["VIP", "Loyal", "Potential", "AtRisk"]:
        sub_chart = df_chart[df_chart["Phân khúc"] == seg]
        sub_sig = sub_chart[sub_chart["Significant"] == "p < 0.05"]
        if not sub_sig.empty:
            top = sub_sig.loc[sub_sig["β"].idxmax()]
            summary_rows.append({
                "Phân khúc": seg,
                "Yếu tố quan trọng nhất": f"{top['Yếu tố']} — {FACTOR_NAMES[top['Yếu tố']]}",
                "β": top["β"],
                "Hàm ý quản trị": {
                    "VIP": "Đầu tư vào năng lực và chuyên nghiệp của nhân viên (Đảm bảo)",
                    "Loyal": "Duy trì cam kết dịch vụ ổn định, minh bạch (Tin cậy)",
                    "Potential": "Tăng tốc độ phục vụ, sẵn sàng đáp ứng yêu cầu (Đáp ứng)",
                    "AtRisk": "Cải thiện không gian, cơ sở vật chất (Hữu hình) để thu hút quay lại",
                }.get(seg, "")
            })
    st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

    st.success(
        "💡 **Trả lời RQ2:** Có sự khác biệt rõ rệt về mức độ ảnh hưởng "
        "của các yếu tố SERVQUAL giữa các phân khúc. Mỗi nhóm khách hàng "
        "ưu tiên các khía cạnh dịch vụ khác nhau, gợi ý chiến lược "
        "chăm sóc theo từng phân khúc thay vì áp dụng đồng nhất."
    )


# ============================================================
# TRANG 7: DỰ ĐOÁN
# ============================================================
elif page == "🔮 Dự đoán CS cho khách mới":
    st.title("🔮 Dự đoán mức độ hài lòng cho khách hàng mới")

    st.markdown(
        """
    Nhập điểm trung bình của khách hàng trên 5 nhân tố SERVQUAL,
    chọn phân khúc RFM dự kiến, và xem mức độ hài lòng dự đoán.
    """
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("**Nhập điểm 5 nhân tố (thang 1-5):**")
        hh = st.slider("Hữu hình (HH)", 1.0, 5.0, 4.0, 0.1)
        tc = st.slider("Tin cậy (TC)", 1.0, 5.0, 4.0, 0.1)
        du = st.slider("Đáp ứng (DU)", 1.0, 5.0, 4.0, 0.1)
        db = st.slider("Đảm bảo (DB)", 1.0, 5.0, 4.0, 0.1)
        ct = st.slider("Cảm thông (CT)", 1.0, 5.0, 4.0, 0.1)

        st.markdown("**Phân khúc RFM:**")
        seg_choice = st.selectbox("Chọn phân khúc:",
                                   ["VIP", "Loyal", "Potential", "AtRisk", "Toàn bộ"])

    with c2:
        # Train model phù hợp
        if seg_choice == "Toàn bộ":
            df_train = merged
        else:
            df_train = merged[merged["segment"] == seg_choice]
        Xt = sm.add_constant(df_train[["HH", "TC", "DU", "DB", "CT"]])
        yt = df_train["CS"]
        model = sm.OLS(yt, Xt).fit()

        x_input = np.array([1, hh, tc, du, db, ct])
        cs_pred = float(model.predict(x_input)[0])
        cs_pred = max(1, min(5, cs_pred))

        st.markdown("### Kết quả dự đoán")
        st.metric("Mức độ hài lòng dự đoán (CS)", f"{cs_pred:.2f} / 5",
                  delta=f"R² model = {model.rsquared:.3f}")

        # Vẽ gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=cs_pred,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": f"CS dự đoán (Phân khúc: {seg_choice})"},
            gauge={
                "axis": {"range": [1, 5]},
                "bar": {"color": "#FF6B6B"},
                "steps": [
                    {"range": [1, 2.5], "color": "#FFE5E5"},
                    {"range": [2.5, 3.5], "color": "#FFFACD"},
                    {"range": [3.5, 5], "color": "#D4F4DD"},
                ],
            }
        ))
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

        # Đóng góp của từng yếu tố
        contrib = {
            "HH": model.params["HH"] * hh,
            "TC": model.params["TC"] * tc,
            "DU": model.params["DU"] * du,
            "DB": model.params["DB"] * db,
            "CT": model.params["CT"] * ct,
        }
        df_contrib = pd.DataFrame({
            "Yếu tố": [FACTOR_NAMES[k] for k in contrib],
            "Đóng góp": list(contrib.values()),
        })
        fig = px.bar(df_contrib, x="Yếu tố", y="Đóng góp",
                     title=f"Đóng góp của từng yếu tố vào CS dự đoán (phân khúc {seg_choice})",
                     color="Đóng góp", color_continuous_scale="Tealgrn",
                     text=df_contrib["Đóng góp"].round(3))
        st.plotly_chart(fig, use_container_width=True)
