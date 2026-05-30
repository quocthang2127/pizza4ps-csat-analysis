# Hướng dẫn deploy lên GitHub + Streamlit Community Cloud

> Mục tiêu cuối: có 2 link để paste vào báo cáo nộp thầy:
> 1. **GitHub repo public** (chứa code + data + README)
> 2. **Streamlit Community Cloud URL** (web app chạy được, ai click cũng xem được)

Cả 2 đều **MIỄN PHÍ**, không cần thẻ tín dụng.

---

## Phần 1 — Hiểu khái niệm trước khi làm

Đoạn này giải thích nhanh để em không bị bỡ ngỡ:

**GitHub** là nơi lưu code online. Em đẩy thư mục dự án lên đó → ai có link cũng xem được code, README, dataset. Repo "public" = ai cũng vào được, không cần login.

**Streamlit Community Cloud** là dịch vụ free do hãng Streamlit cung cấp: em **kết nối GitHub repo của em vào Streamlit Cloud**, nó tự động:
1. Đọc file `requirements.txt` để cài thư viện
2. Chạy lệnh `streamlit run app/app.py`
3. Cấp cho em một URL public dạng `https://<tên-app>.streamlit.app`

Khi em sửa code rồi `git push` lên GitHub, Streamlit Cloud **tự rebuild** trong ~1 phút. Đúng nghĩa "deploy continuous" miễn phí.

Tóm lại quy trình: **viết code local → push lên GitHub → kết nối Streamlit Cloud → có URL public**.

---

## Phần 2 — Cài đặt một lần (~15 phút)

### Bước 1: Tạo tài khoản GitHub

1. Vào https://github.com/signup
2. Đăng ký bằng email (nếu chưa có)
3. Verify email
4. (Khuyến nghị) Bật 2FA cho an toàn

### Bước 2: Cài Git trên máy

**macOS:**
```bash
# Mở Terminal, gõ:
git --version
# Nếu báo "command not found" thì cài:
xcode-select --install
```

**Windows:** tải từ https://git-scm.com/download/win, cài mặc định.

### Bước 3: Cấu hình Git lần đầu

Mở Terminal/PowerShell, gõ (thay tên + email của em):
```bash
git config --global user.name "Đặng Duy Quốc Thắng"
git config --global user.email "quocthang2127@gmail.com"
```

### Bước 4: Tạo personal access token (thay cho password khi push)

GitHub không cho dùng password để push từ 2021. Em cần tạo **Personal Access Token (PAT)**:

1. Vào https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Note: `Streamlit deploy`, Expiration: 90 days
4. Tick quyền **`repo`** (Full control of private repositories)
5. Click **Generate token** → copy token (ví dụ `ghp_xxxxxxxxxxxxx`) → **lưu lại** vào Notes/file riêng (chỉ hiện 1 lần)

---

## Phần 3 — Push code lên GitHub (~5 phút)

### Bước 5: Tạo repo mới trên GitHub

1. Vào https://github.com/new
2. Repository name: `pizza4ps-csat-analysis`
3. Description: `Phân tích sự hài lòng khách hàng Pizza 4P's bằng SERVQUAL + RFM`
4. Chọn **Public** ✅
5. **KHÔNG** tick "Add README" / "Add .gitignore" (vì mình đã có sẵn rồi)
6. Click **Create repository**
7. Sẽ thấy trang trống — copy URL repo (dạng `https://github.com/<username>/pizza4ps-csat-analysis.git`)

### Bước 6: Push code từ máy local lên GitHub

Mở Terminal, vào thư mục dự án:

```bash
cd "/Users/quocthang/Documents/Claude/Projects/Master-Study-IDT/Pizza4Ps_DataMining"

# Khởi tạo git repo
git init
git branch -M main

# Add toàn bộ file (trừ những thứ trong .gitignore)
git add .
git commit -m "Initial commit: Pizza 4P's CSAT analysis with SERVQUAL + RFM"

# Kết nối với repo trên GitHub (thay <username>)
git remote add origin https://github.com/<username>/pizza4ps-csat-analysis.git

# Push lên
git push -u origin main
```

Khi nó hỏi:
- Username: `<username GitHub của em>`
- Password: **paste Personal Access Token** (PAT đã tạo ở Bước 4), KHÔNG phải password GitHub thật

Sau khi push xong, vào https://github.com/<username>/pizza4ps-csat-analysis sẽ thấy toàn bộ file.

> **Mẹo:** trên Mac có thể lưu PAT vào keychain để không phải nhập lại:
> ```bash
> git config --global credential.helper osxkeychain
> ```

---

## Phần 4 — Deploy lên Streamlit Community Cloud (~3 phút)

### Bước 7: Đăng ký Streamlit Cloud

1. Vào https://streamlit.io/cloud
2. Click **Sign up** → **Continue with GitHub** (login bằng tài khoản GitHub đã tạo)
3. Cho phép Streamlit truy cập danh sách repo của em

### Bước 8: Tạo app

1. Sau khi vào dashboard, click **New app**
2. Điền:
   - **Repository:** chọn `<username>/pizza4ps-csat-analysis`
   - **Branch:** `main`
   - **Main file path:** `app/app.py`
   - **App URL (custom):** ví dụ `pizza4ps-csat`
3. Click **Deploy!**

### Bước 9: Đợi build (~1-2 phút)

Streamlit Cloud sẽ:
1. Clone repo
2. Cài thư viện theo `requirements.txt`
3. Chạy `streamlit run app/app.py`

Khi xong em sẽ có URL dạng `https://pizza4ps-csat.streamlit.app`. Click thử để xem.

---

## Phần 5 — Cập nhật về sau

Bất cứ khi nào em muốn sửa code/data:

```bash
cd "/Users/quocthang/Documents/Claude/Projects/Master-Study-IDT/Pizza4Ps_DataMining"

# Sửa file...

git add .
git commit -m "Update: <mô tả ngắn>"
git push
```

Streamlit Cloud sẽ tự rebuild trong ~1 phút.

---

## Phần 6 — Xử lý lỗi thường gặp

**Lỗi 1: Streamlit Cloud build fail vì thiếu thư viện**
→ Mở `requirements.txt`, kiểm tra đã có đủ chưa. Push lại.

**Lỗi 2: `ModuleNotFoundError: No module named 'app'`**
→ Đường dẫn trong "Main file path" sai. Phải đúng là `app/app.py`.

**Lỗi 3: App load chậm lần đầu**
→ Bình thường (cold start ~30s). Lần sau nhanh.

**Lỗi 4: Repo private không deploy được**
→ Free tier chỉ hỗ trợ public repo. Đổi thành public trong Settings.

**Lỗi 5: `git push` báo "Authentication failed"**
→ Em đang nhập password GitHub thật. Phải nhập **Personal Access Token** (PAT) ở Bước 4.

**Lỗi 6: File data quá lớn (>100MB)**
→ Không phải vấn đề ở project này (data <5MB), nhưng nếu sau này có file lớn thì dùng [Git LFS](https://git-lfs.com).

---

## Phần 7 — Kiểm tra cuối cùng

Trước khi nộp bài, đảm bảo:

- [ ] Repo public (ai click cũng xem được mà không cần login)
- [ ] README hiển thị đẹp ở trang chủ repo
- [ ] Streamlit URL chạy được trên trình duyệt khác (ẩn danh / điện thoại)
- [ ] Tất cả 7 trang trong sidebar đều click được không lỗi
- [ ] Trên báo cáo paper có ghi cả 2 link: GitHub repo + Streamlit URL

---

## Phần 8 — Cách paste vào báo cáo

Trong section cuối paper (hoặc footnote), thêm dòng:

```
Source code & live demo:
- GitHub: https://github.com/<username>/pizza4ps-csat-analysis
- Live demo: https://pizza4ps-csat.streamlit.app
```

Có thể thêm QR code (dùng https://www.qr-code-generator.com) cho thầy quét trong khi thuyết trình.
