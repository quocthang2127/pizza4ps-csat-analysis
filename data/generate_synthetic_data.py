"""
Sinh synthetic dataset cho nghiên cứu:
"Phân tích các yếu tố ảnh hưởng đến sự hài lòng và sự khác biệt
 giữa các nhóm khách hàng tại Pizza 4P's"

Tác giả: Đặng Duy Quốc Thắng
Mục đích: Mô phỏng dữ liệu phục vụ học thuật (academic demonstration).

Data được sinh có cấu trúc khoa học:
- 5 nhân tố SERVQUAL có correlation nội tại cao giữa các biến quan sát cùng nhóm
  (để Cronbach's Alpha và EFA cho kết quả hợp lý)
- Customer base được chia thành 4 phân khúc RFM với hành vi khác nhau:
    * VIP (high R, F, M)
    * Loyal (medium-high F, M, recent)
    * Potential (medium, recent but low F)
    * At-risk/New (old R, low F, M)
- Mỗi phân khúc có hệ số hồi quy β khác nhau (segment-specific effects),
  ví dụ VIP nhạy cảm với DB (Đảm bảo) hơn, Potential nhạy cảm với DU (Đáp ứng) hơn
  → để bài phân tích có insight để discuss khi so sánh giữa các phân khúc.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Reproducibility
np.random.seed(42)

# -------------------------- CẤU HÌNH --------------------------
N_CUSTOMERS = 600
ANALYSIS_DATE = datetime(2025, 12, 31)  # ngày tham chiếu để tính Recency

# Biến quan sát (observed items) cho từng nhân tố SERVQUAL
ITEMS = {
    "HH": ["HH1", "HH2", "HH3", "HH4"],         # Hữu hình (4 items)
    "TC": ["TC1", "TC2", "TC3", "TC4"],         # Tin cậy (4 items)
    "DU": ["DU1", "DU2", "DU3", "DU4"],         # Đáp ứng (4 items)
    "DB": ["DB1", "DB2", "DB3", "DB4"],         # Đảm bảo (4 items)
    "CT": ["CT1", "CT2", "CT3"],                # Cảm thông (3 items)
}
CS_ITEMS = ["CS1", "CS2", "CS3"]                # Customer Satisfaction (3 items)

# Phân phối phân khúc (giống Pareto thực tế trong F&B)
SEGMENT_DIST = {
    "VIP":       0.10,   # 10% — chi nhiều, đến nhiều, gần đây
    "Loyal":     0.25,   # 25% — trung thành
    "Potential": 0.35,   # 35% — tiềm năng, mới chăm
    "AtRisk":    0.30,   # 30% — đã lâu chưa quay lại / khách mới ít tương tác
}

# Hệ số hồi quy "ngầm" (latent) cho từng phân khúc
# CS = β0 + β_HH*HH + β_TC*TC + β_DU*DU + β_DB*DB + β_CT*CT + ε
# Đã chuẩn hóa để Σβ ≈ 1 và mỗi phân khúc có 1-2 yếu tố nổi trội rõ rệt
SEGMENT_BETAS = {
    # VIP rất quan trọng Đảm bảo (DB) và Cảm thông (CT) — họ trả tiền cao,
    # kỳ vọng nhân viên am hiểu, chuyên nghiệp, quan tâm cá nhân
    "VIP":       {"intercept": 0.20, "HH": 0.05, "TC": 0.10, "DU": 0.05, "DB": 0.45, "CT": 0.30},
    # Loyal nhạy cảm với Tin cậy (TC) — họ kỳ vọng dịch vụ ổn định, đúng cam kết
    "Loyal":     {"intercept": 0.30, "HH": 0.08, "TC": 0.45, "DU": 0.10, "DB": 0.15, "CT": 0.15},
    # Potential rất nhạy cảm với Đáp ứng (DU) — khách mới quan tâm tốc độ, sẵn sàng phục vụ
    "Potential": {"intercept": 0.25, "HH": 0.12, "TC": 0.10, "DU": 0.45, "DB": 0.10, "CT": 0.15},
    # AtRisk nhạy cảm Hữu hình (HH) — không gian ấn tượng có thể kéo họ quay lại
    "AtRisk":    {"intercept": 0.35, "HH": 0.40, "TC": 0.15, "DU": 0.15, "DB": 0.10, "CT": 0.12},
}

# RFM "ngầm" cho mỗi phân khúc (mean ± std)
SEGMENT_RFM = {
    # Recency tính bằng ngày kể từ giao dịch gần nhất tới ANALYSIS_DATE (càng nhỏ càng tốt)
    # Frequency: số lần giao dịch trong 12 tháng
    # Monetary: tổng chi tiêu (VND)
    "VIP":       {"R_mean": 15,  "R_std": 8,   "F_mean": 18, "F_std": 5,  "M_mean": 9_500_000, "M_std": 2_500_000},
    "Loyal":     {"R_mean": 35,  "R_std": 15,  "F_mean": 9,  "F_std": 3,  "M_mean": 4_200_000, "M_std": 1_200_000},
    "Potential": {"R_mean": 50,  "R_std": 20,  "F_mean": 4,  "F_std": 1,  "M_mean": 1_800_000, "M_std":   600_000},
    "AtRisk":    {"R_mean": 180, "R_std": 60,  "F_mean": 2,  "F_std": 1,  "M_mean":   900_000, "M_std":   400_000},
}

# Mean "ngầm" của mỗi nhân tố SERVQUAL theo phân khúc (trên thang 1-5)
# (VIP đánh giá tổng thể tốt hơn vì thường là khách quen được phục vụ kỹ)
SEGMENT_FACTOR_MEANS = {
    "VIP":       {"HH": 4.30, "TC": 4.40, "DU": 4.20, "DB": 4.50, "CT": 4.40},
    "Loyal":     {"HH": 4.10, "TC": 4.25, "DU": 4.00, "DB": 4.10, "CT": 4.15},
    "Potential": {"HH": 3.95, "TC": 3.85, "DU": 4.05, "DB": 3.95, "CT": 3.90},
    "AtRisk":    {"HH": 3.70, "TC": 3.60, "DU": 3.55, "DB": 3.65, "CT": 3.60},
}


# -------------------------- SINH DỮ LIỆU --------------------------

def assign_segments(n: int) -> np.ndarray:
    """Gán phân khúc cho từng customer theo phân phối SEGMENT_DIST."""
    segments = list(SEGMENT_DIST.keys())
    probs = list(SEGMENT_DIST.values())
    return np.random.choice(segments, size=n, p=probs)


def generate_factor_scores(segment: str) -> dict:
    """Sinh điểm trung bình ngầm cho 5 nhân tố của một customer thuộc segment."""
    means = SEGMENT_FACTOR_MEANS[segment]
    # mỗi nhân tố lệch quanh mean của segment với độ lệch chuẩn nhỏ
    return {f: np.clip(np.random.normal(mu, 0.45), 1, 5) for f, mu in means.items()}


def generate_observed_items(factor_scores: dict) -> dict:
    """
    Từ điểm latent của 5 nhân tố, sinh điểm trên các biến quan sát Likert 5 điểm.
    Cộng thêm noise nhỏ cho từng item để có biến thiên trong cùng nhân tố,
    nhưng vẫn giữ tương quan cao (để Cronbach's Alpha cao).
    """
    items = {}
    for factor, item_list in ITEMS.items():
        latent = factor_scores[factor]
        for item in item_list:
            # noise std nhỏ → tương quan trong nhóm cao → Cronbach Alpha cao
            score = np.random.normal(latent, 0.35)
            score = int(np.clip(round(score), 1, 5))
            items[item] = score
    return items


def generate_cs_items(segment: str, factor_scores: dict) -> tuple:
    """
    Sinh CS items dựa trên công thức tuyến tính ngầm:
    CS_latent = intercept + Σ β_f * factor_f + noise
    Sau đó scale về thang 1-5 và sinh 3 CS items quanh giá trị này.
    """
    betas = SEGMENT_BETAS[segment]
    cs_latent = (
        betas["intercept"]
        + betas["HH"] * factor_scores["HH"]
        + betas["TC"] * factor_scores["TC"]
        + betas["DU"] * factor_scores["DU"]
        + betas["DB"] * factor_scores["DB"]
        + betas["CT"] * factor_scores["CT"]
        + np.random.normal(0, 0.18)  # noise tổng (vừa phải để ra R² ~0.55-0.7)
    )
    cs_latent = float(np.clip(cs_latent, 1, 5))
    items = {}
    for it in CS_ITEMS:
        items[it] = int(np.clip(round(np.random.normal(cs_latent, 0.30)), 1, 5))
    return cs_latent, items


def generate_rfm(segment: str) -> tuple:
    """Sinh R (ngày), F (số lần), M (VND) cho customer."""
    p = SEGMENT_RFM[segment]
    R = max(1, int(np.random.normal(p["R_mean"], p["R_std"])))
    F = max(1, int(np.random.normal(p["F_mean"], p["F_std"])))
    M = max(100_000, int(np.random.normal(p["M_mean"], p["M_std"])))
    return R, F, M


def generate_pos_transactions(customer_id: str, R: int, F: int, M: int) -> list:
    """
    Sinh F giao dịch trong vòng 12 tháng gần đây.
    Giao dịch gần nhất cách ANALYSIS_DATE đúng R ngày.
    Tổng các transaction xấp xỉ M.
    """
    last_date = ANALYSIS_DATE - timedelta(days=R)
    # phân bổ M ngẫu nhiên cho F giao dịch (Dirichlet để tổng = 1)
    weights = np.random.dirichlet(np.ones(F) * 1.5)
    amounts = (weights * M).astype(int)
    # các ngày giao dịch khác phân bố ngẫu nhiên trong 365 ngày trước last_date
    other_dates = sorted(
        [last_date - timedelta(days=int(np.random.uniform(1, 365))) for _ in range(F - 1)]
    )
    dates = other_dates + [last_date]
    rows = []
    for d, a in zip(dates, amounts):
        rows.append({
            "customer_id": customer_id,
            "transaction_date": d.strftime("%Y-%m-%d"),
            "amount_vnd": int(a),
        })
    return rows


# -------------------------- MAIN --------------------------

def main():
    # 1) Sinh customer + survey
    segments = assign_segments(N_CUSTOMERS)
    survey_rows = []
    pos_rows = []
    rfm_truth_rows = []  # chỉ để debug/tham chiếu, không dùng cho phân tích

    # demographic columns thêm để bài phong phú hơn
    age_choices = ["18-24", "25-34", "35-44", "45-54", "55+"]
    age_probs = [0.20, 0.40, 0.25, 0.10, 0.05]
    gender_choices = ["Nam", "Nữ"]
    visit_freq_choices = ["Lần đầu", "Thỉnh thoảng", "Thường xuyên", "Rất thường xuyên"]

    for i, seg in enumerate(segments):
        cid = f"C{i+1:04d}"

        # 1a) sinh điểm latent cho 5 nhân tố
        factor_scores = generate_factor_scores(seg)

        # 1b) sinh các biến quan sát SERVQUAL (Likert 1-5)
        obs_items = generate_observed_items(factor_scores)

        # 1c) sinh CS items (1-5) dựa trên công thức ngầm
        cs_latent, cs_items = generate_cs_items(seg, factor_scores)

        # 1d) sinh RFM
        R, F, M = generate_rfm(seg)
        pos_rows.extend(generate_pos_transactions(cid, R, F, M))
        rfm_truth_rows.append({"customer_id": cid, "segment_truth": seg, "R": R, "F": F, "M": M})

        # demographics
        age = np.random.choice(age_choices, p=age_probs)
        gender = np.random.choice(gender_choices, p=[0.45, 0.55])
        visit_freq = np.random.choice(visit_freq_choices, p=[0.15, 0.40, 0.30, 0.15])

        row = {"customer_id": cid, "age_group": age, "gender": gender, "visit_freq": visit_freq}
        row.update(obs_items)
        row.update(cs_items)
        survey_rows.append(row)

    survey_df = pd.DataFrame(survey_rows)
    pos_df = pd.DataFrame(pos_rows).sort_values(["customer_id", "transaction_date"]).reset_index(drop=True)
    truth_df = pd.DataFrame(rfm_truth_rows)

    # 2) Lưu file (lưu cùng thư mục với script này)
    import os
    out_dir = os.path.dirname(os.path.abspath(__file__))
    survey_df.to_csv(f"{out_dir}/survey_servqual.csv", index=False, encoding="utf-8-sig")
    pos_df.to_csv(f"{out_dir}/pos_transactions.csv", index=False, encoding="utf-8-sig")
    truth_df.to_csv(f"{out_dir}/_segment_ground_truth.csv", index=False, encoding="utf-8-sig")

    print(f"✓ Survey:        {survey_df.shape[0]} rows × {survey_df.shape[1]} cols")
    print(f"✓ POS:           {pos_df.shape[0]} rows × {pos_df.shape[1]} cols")
    print(f"✓ Ground truth:  {truth_df.shape[0]} rows (chỉ dùng để verify, KHÔNG dùng trong phân tích)")
    print("\nPhân bố phân khúc thực:")
    print(truth_df["segment_truth"].value_counts(normalize=True).round(3))

    print("\nMẫu survey (3 dòng đầu):")
    print(survey_df.head(3))

    print("\nMẫu POS (3 dòng đầu):")
    print(pos_df.head(3))


if __name__ == "__main__":
    main()
