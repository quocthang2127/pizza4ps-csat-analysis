# Pizza 4P's - Customer Satisfaction Analysis

**Đề tài:** Phân tích các yếu tố ảnh hưởng đến sự hài lòng và sự khác biệt giữa các nhóm khách hàng tại Pizza 4P's (kết hợp **SERVQUAL** + **RFM**).

**Tác giả:** Đặng Duy Quốc Thắng - Ngô Xuân Vinh - Nguyễn Bá Đức
**Môn học:** Khai phá dữ liệu nâng cao - Cao học IDT
**GVHD:** TS. Võ Văn Hải

---

## Demo

Web app: `https:/pizza4ps-csat.streamlit.app` *(điền sau khi deploy)*
GitHub repo: `https://github.com/quocthang2127/pizza4ps-csat-analysis` 

## Cách chạy local

```bash
# 1. Cài dependencies
pip install -r requirements.txt

# 2. (Tùy chọn) Sinh lại dataset
python data/generate_synthetic_data.py

# 3. Chạy pipeline phân tích - kết quả lưu vào data/results/
python notebooks/analysis_pipeline.py

# 4. Mở web app
streamlit run app/app.py
```

App sẽ mở tại `http://localhost:8501`.

## Phương pháp

1. **Cronbach's Alpha** - kiểm định độ tin cậy thang đo (5 nhân tố SERVQUAL + CS)
2. **EFA (Exploratory Factor Analysis)** - kiểm tra cấu trúc nhân tố (KMO, Bartlett, varimax rotation)
3. **Multiple Linear Regression** trên toàn bộ mẫu - trả lời RQ1
4. **K-Means trên RFM** - phân khúc 4 nhóm khách hàng
5. **MLR theo từng phân khúc + so sánh hệ số β** - trả lời RQ2

## Kết quả chính

- Cả 5 yếu tố SERVQUAL đều ảnh hưởng có ý nghĩa thống kê đến sự hài lòng (p < 0.001 toàn mẫu)
- **VIP** ưu tiên *Đảm bảo*; **Loyal** ưu tiên *Tin cậy*; **Potential** ưu tiên *Đáp ứng*; **AtRisk** ưu tiên *Hữu hình*
- Gợi ý chiến lược chăm sóc khách hàng theo từng phân khúc thay vì áp dụng đồng nhất

## Lưu ý

Dataset trong repo này là **synthetic data** được sinh phục vụ học thuật, không phải dữ liệu thật của Pizza 4P's. Cấu trúc tương quan và phân khúc được thiết kế mô phỏng để bài toán có ý nghĩa khi phân tích.
