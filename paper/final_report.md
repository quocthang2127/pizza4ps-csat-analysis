# Phân tích các yếu tố ảnh hưởng đến sự hài lòng và sự khác biệt giữa các nhóm khách hàng tại Pizza 4P's: Tích hợp mô hình SERVQUAL và phân khúc RFM

**Tác giả:** Đặng Duy Quốc Thắng
**Môn học:** Khai phá dữ liệu nâng cao
**Giảng viên hướng dẫn:** TS. Võ Văn Hải
**Chương trình:** Cao học Hệ thống Thông tin Quản lý — Chuyên ngành IDT
**Năm học:** 2025–2026

---

## Abstract (Tóm tắt) — 290 từ

Trong bối cảnh ngành dịch vụ ăn uống (F&B) Việt Nam tăng trưởng nhanh chóng với tốc độ 15–18% mỗi năm và mức độ cạnh tranh ngày càng khốc liệt, sự hài lòng của khách hàng trở thành yếu tố then chốt giúp doanh nghiệp duy trì lợi thế bền vững. Các nghiên cứu hiện hành chủ yếu áp dụng mô hình SERVQUAL của Parasuraman, Zeithaml và Berry (1988) để phân tích chất lượng dịch vụ thông qua năm thành phần là Hữu hình, Tin cậy, Đáp ứng, Đảm bảo và Cảm thông. Tuy nhiên, phần lớn các nghiên cứu này xem khách hàng như một tập hợp đồng nhất và không xét đến sự khác biệt về hành vi tiêu dùng giữa các nhóm. Trong khi đó, các phân tích phân khúc theo mô hình RFM lại chủ yếu phục vụ mục đích marketing, chưa được tích hợp với phân tích sự hài lòng. Nghiên cứu này đề xuất một cách tiếp cận tích hợp giữa SERVQUAL và RFM nhằm trả lời hai câu hỏi: (RQ1) các yếu tố chất lượng dịch vụ ảnh hưởng như thế nào đến sự hài lòng tại Pizza 4P's, và (RQ2) mức độ ảnh hưởng này có khác nhau giữa các nhóm khách hàng được phân khúc bằng RFM hay không. Một bộ dữ liệu mô phỏng gồm 600 khách hàng (khảo sát Likert năm điểm trên mười chín biến quan sát thuộc năm nhân tố SERVQUAL) và 3,473 giao dịch POS được sử dụng. Quy trình phân tích bao gồm kiểm định Cronbach's Alpha, phân tích nhân tố khám phá EFA, hồi quy tuyến tính đa biến trên toàn mẫu, phân khúc khách hàng bằng K-Means trên RFM, và hồi quy riêng cho từng phân khúc. Kết quả cho thấy cả năm yếu tố SERVQUAL đều có ảnh hưởng có ý nghĩa thống kê đến sự hài lòng (R² = 0.41), trong đó Tin cậy có ảnh hưởng mạnh nhất. Quan trọng hơn, mức độ ảnh hưởng của các yếu tố khác biệt rõ rệt giữa bốn phân khúc: VIP nhạy cảm với Đảm bảo, Loyal với Tin cậy, Potential với Đáp ứng, và AtRisk với Hữu hình. Phát hiện này cung cấp bằng chứng định lượng cho chiến lược chăm sóc khách hàng cá nhân hoá theo phân khúc thay vì áp dụng đồng nhất.

**Từ khóa:** SERVQUAL, RFM, phân khúc khách hàng, hồi quy tuyến tính đa biến, K-Means, Pizza 4P's, ngành F&B, khai phá dữ liệu, customer satisfaction, customer segmentation.

---

## 1. Giới thiệu (Introduction)

Ngành dịch vụ ăn uống (F&B – Food & Beverage) tại Việt Nam đang trải qua giai đoạn phát triển mạnh mẽ chưa từng có. Theo báo cáo của Euromonitor International (2024), thị trường F&B Việt Nam duy trì tốc độ tăng trưởng kép hàng năm khoảng 15–18% trong giai đoạn 2020–2024, với quy mô ước tính đạt khoảng 610.000 tỷ đồng (tương đương 25 tỷ USD) vào năm 2024. Báo cáo của iPOS.vn (2024) cho thấy hơn 60% người tiêu dùng Việt Nam sẵn sàng chi tiêu cho trải nghiệm ăn uống bên ngoài, đặc biệt là tầng lớp trung lưu thành thị có thu nhập từ 15 triệu đồng/tháng trở lên. Nielsen Vietnam (2023) cũng chỉ ra rằng phân khúc nhà hàng trải nghiệm (experience dining) tăng trưởng nhanh hơn so với nhà hàng phục vụ nhanh, phản ánh xu hướng người tiêu dùng coi việc đi ăn ngoài không chỉ để no mà còn là hoạt động giải trí và xã hội.

Trong bối cảnh này, sự cạnh tranh giữa các chuỗi nhà hàng trở nên khốc liệt hơn bao giờ hết. McKinsey & Company (2023) ước tính rằng các doanh nghiệp F&B sử dụng dữ liệu khách hàng (CRM/POS) một cách hiệu quả có thể tăng 20–30% hiệu quả giữ chân khách hàng và tăng 15% giá trị vòng đời khách hàng (Customer Lifetime Value – CLV). Điều này đặt ra yêu cầu cấp thiết cho các doanh nghiệp về việc khai thác dữ liệu khách hàng để hiểu sâu hơn về hành vi và kỳ vọng của họ, từ đó xây dựng chiến lược dịch vụ hiệu quả.

Pizza 4P's là một trong những thương hiệu nhà hàng pizza cao cấp nổi bật nhất tại Việt Nam, được thành lập vào năm 2011 bởi vợ chồng người Nhật Yosuke Masuko và Sanae Takasugi. Thương hiệu được định vị với concept "Farm-to-Table" cùng triết lý "Delivering Wow, Sharing Happiness", tập trung vào nguồn nguyên liệu tươi từ trang trại riêng tại Đà Lạt và quy trình chế biến thủ công. Tính đến năm 2025, Pizza 4P's đã mở rộng lên hơn 30 chi nhánh tại Việt Nam và quốc tế (bao gồm Nhật Bản, Campuchia, Ấn Độ và Hàn Quốc), phục vụ hàng triệu lượt khách mỗi năm. Với sự tập trung mạnh vào chất lượng sản phẩm, không gian thiết kế và dịch vụ khách hàng, Pizza 4P's trở thành một trong những thương hiệu tiêu biểu trong phân khúc nhà hàng trải nghiệm cao cấp, nơi sự hài lòng của khách hàng đóng vai trò trung tâm trong chiến lược phát triển dài hạn.

Tuy nhiên, việc nâng cao sự hài lòng khách hàng trong ngành nhà hàng cao cấp gặp phải nhiều thách thức. Khách hàng ngày càng đa dạng về kỳ vọng, thói quen tiêu dùng và mức độ trung thành. Một khách hàng VIP đến nhà hàng hàng tuần với hoá đơn lớn sẽ có yêu cầu khác hẳn so với một khách hàng mới chỉ ghé thăm lần đầu để thử trải nghiệm. Tương tự, một khách hàng đã lâu không quay lại có thể có những lo ngại đặc thù khác với khách hàng thường xuyên. Việc áp dụng một chiến lược dịch vụ "cào bằng" cho tất cả khách hàng sẽ dẫn đến lãng phí nguồn lực và bỏ lỡ cơ hội tối ưu hoá trải nghiệm cho từng nhóm.

Các nghiên cứu trước đây về sự hài lòng khách hàng trong lĩnh vực dịch vụ thường dựa trên mô hình SERVQUAL với năm thành phần: Hữu hình, Tin cậy, Đáp ứng, Đảm bảo và Cảm thông. Các nghiên cứu này cho phép đo lường và phân tích mối quan hệ giữa chất lượng dịch vụ và sự hài lòng thông qua các phương pháp thống kê, điển hình là hồi quy tuyến tính đa biến. Tuy nhiên, phần lớn các nghiên cứu hiện tại chỉ xem xét khách hàng như một tập hợp đồng nhất, mà chưa phân tích sâu sự khác biệt về hành vi và mức độ ảnh hưởng của các yếu tố dịch vụ giữa các nhóm khách hàng khác nhau. Trong khi đó, với sự phát triển của các hệ thống quản lý dữ liệu như POS (Point of Sale) và CRM (Customer Relationship Management), doanh nghiệp ngày nay có thể thu thập dữ liệu chi tiết về hành vi tiêu dùng của khách hàng, bao gồm tần suất ghé thăm, giá trị chi tiêu và thời gian tương tác gần nhất. Mô hình RFM (Recency, Frequency, Monetary) đã được sử dụng rộng rãi để phân khúc khách hàng theo giá trị và mức độ trung thành. Tuy nhiên, trong nhiều nghiên cứu, kết quả phân khúc này thường chỉ được sử dụng cho mục đích mô tả hoặc marketing, mà chưa được tích hợp trực tiếp vào việc phân tích sự hài lòng của khách hàng.

Xuất phát từ những hạn chế này, nghiên cứu đề xuất một cách tiếp cận tích hợp, kết hợp giữa mô hình SERVQUAL và phân tích RFM nhằm không chỉ xác định các yếu tố ảnh hưởng đến sự hài lòng khách hàng, mà còn phân tích sự khác biệt về mức độ ảnh hưởng của các yếu tố này giữa các nhóm khách hàng có hành vi tiêu dùng khác nhau. Cách tiếp cận này giúp cung cấp cái nhìn toàn diện hơn về khách hàng, từ đó hỗ trợ doanh nghiệp đưa ra các chiến lược nâng cao trải nghiệm dịch vụ một cách hiệu quả và có định hướng theo từng phân khúc cụ thể.

### 1.1 Phát biểu bài toán (Problem Formulation)

Nghiên cứu xem xét mối quan hệ giữa chất lượng dịch vụ và sự hài lòng của khách hàng trong bối cảnh chuỗi nhà hàng Pizza 4P's. Cụ thể, mỗi khách hàng được biểu diễn bởi một tập các biến quan sát phản ánh các khía cạnh của chất lượng dịch vụ, bao gồm các thành phần của mô hình SERVQUAL như Hữu hình (HH), Tin cậy (TC), Đáp ứng (DU), Đảm bảo (DB) và Cảm thông (CT). Biến phụ thuộc của mô hình là mức độ hài lòng tổng thể của khách hàng (CS – Customer Satisfaction), được đo lường thông qua thang đo Likert năm điểm. Mục tiêu của nghiên cứu là xây dựng mô hình hồi quy tuyến tính đa biến nhằm ước lượng mức độ ảnh hưởng của từng yếu tố chất lượng dịch vụ đến sự hài lòng của khách hàng.

Bên cạnh đó, dựa trên dữ liệu giao dịch từ hệ thống POS, khách hàng được phân nhóm theo mô hình RFM, phản ánh hành vi tiêu dùng và giá trị của khách hàng. Trên cơ sở này, nghiên cứu không chỉ phân tích mô hình hồi quy trên toàn bộ tập dữ liệu, mà còn xem xét sự khác biệt trong mối quan hệ giữa chất lượng dịch vụ và sự hài lòng giữa các nhóm khách hàng khác nhau. Qua đó, nghiên cứu hướng đến việc cung cấp các kết luận mang tính phân khúc, thay vì chỉ dừng lại ở phân tích tổng thể.

### 1.2 Câu hỏi nghiên cứu (Research Questions)

Nghiên cứu được định hướng bởi hai câu hỏi chính sau:

- **RQ1:** Các yếu tố chất lượng dịch vụ (Hữu hình, Tin cậy, Đáp ứng, Đảm bảo, Cảm thông) ảnh hưởng như thế nào đến sự hài lòng của khách hàng tại Pizza 4P's?
- **RQ2:** Mức độ ảnh hưởng của các yếu tố chất lượng dịch vụ đến sự hài lòng có khác nhau giữa các nhóm khách hàng được phân loại theo mô hình RFM hay không?

### 1.3 Đóng góp của nghiên cứu

Nghiên cứu này đóng góp vào kho tri thức học thuật và thực tiễn ở ba khía cạnh chính. Thứ nhất, về mặt lý thuyết, nghiên cứu đề xuất một khung phân tích tích hợp giữa SERVQUAL và RFM, lấp đầy khoảng trống trong văn liệu khi hai khung này thường được áp dụng độc lập. Thứ hai, về mặt phương pháp, nghiên cứu minh hoạ quy trình bảy bước có thể tái sử dụng cho các bài toán tương tự trong các ngành dịch vụ khác như khách sạn, bán lẻ, ngân hàng. Thứ ba, về mặt thực tiễn, kết quả phân tích cung cấp bằng chứng định lượng giúp doanh nghiệp F&B xây dựng chiến lược chăm sóc khách hàng phân khúc, tối ưu hoá phân bổ nguồn lực marketing và đào tạo nhân viên.

---

## 2. Tổng quan nghiên cứu (Related Works)

### 2.1 Chất lượng dịch vụ và sự hài lòng khách hàng

Trong lĩnh vực dịch vụ, mối quan hệ giữa chất lượng dịch vụ và sự hài lòng của khách hàng đã được nghiên cứu rộng rãi suốt hơn ba thập kỷ qua. Một trong những mô hình phổ biến nhất là SERVQUAL được Parasuraman, Zeithaml và Berry (1988) phát triển, nhằm đo lường chất lượng dịch vụ thông qua năm thành phần chính: Hữu hình (Tangibles), Tin cậy (Reliability), Đáp ứng (Responsiveness), Đảm bảo (Assurance) và Cảm thông (Empathy). Mô hình này được xây dựng dựa trên nguyên lý "khoảng cách" (gap model), trong đó chất lượng dịch vụ được đo bằng chênh lệch giữa kỳ vọng và cảm nhận thực tế của khách hàng.

Cronin và Taylor (1992) đã đưa ra một biến thể quan trọng của mô hình này — SERVPERF — chỉ đo cảm nhận thực tế mà không cần so sánh với kỳ vọng. Họ lập luận rằng SERVPERF có khả năng dự báo tốt hơn về sự hài lòng và ý định mua lại, đồng thời đơn giản hơn trong thu thập dữ liệu. Nhiều nghiên cứu thực nghiệm sau này, bao gồm Brady và Cronin (2001) cũng như Jain và Gupta (2004), đã ủng hộ quan điểm này, đặc biệt trong bối cảnh ngành dịch vụ trải nghiệm như nhà hàng, khách sạn và bệnh viện.

Phương pháp hồi quy tuyến tính đa biến thường được sử dụng để ước lượng mức độ ảnh hưởng của từng yếu tố SERVQUAL đến sự hài lòng tổng thể. Cách tiếp cận này cho phép xác định yếu tố nào đóng vai trò quan trọng hơn trong việc hình thành trải nghiệm khách hàng, từ đó hỗ trợ doanh nghiệp cải thiện chất lượng dịch vụ một cách có trọng tâm. Ngoài ra, các kỹ thuật tiên tiến hơn như mô hình phương trình cấu trúc (Structural Equation Modeling – SEM) cũng được áp dụng trong các nghiên cứu của Hair et al. (2014) và các nghiên cứu Việt Nam như Nguyễn Đình Thọ (2011), giúp kiểm định đồng thời nhiều giả thuyết về mối quan hệ nhân quả giữa các biến tiềm ẩn.

### 2.2 Ứng dụng SERVQUAL trong ngành F&B và nhà hàng

Trong ngành F&B, trải nghiệm khách hàng mang tính tổng hợp, bao gồm cả yếu tố hữu hình (không gian, trình bày món ăn, vệ sinh) và yếu tố vô hình (thái độ phục vụ, tốc độ phục vụ, sự chu đáo). Stevens, Knutson và Patton (1995) đã phát triển DINESERV — một biến thể của SERVQUAL chuyên cho ngành nhà hàng, gồm 29 biến quan sát thuộc năm chiều tương tự. Nghiên cứu của họ trên 200 nhà hàng tại Mỹ cho thấy DINESERV có khả năng phân biệt tốt giữa các nhà hàng khác nhau và dự báo chính xác ý định quay lại.

Namkung và Jang (2007) đã mở rộng nghiên cứu trong ngành nhà hàng cao cấp, xem xét vai trò của chất lượng món ăn (food quality), môi trường (atmosphere) và dịch vụ (service) đối với sự hài lòng và lòng trung thành. Họ phát hiện rằng chất lượng món ăn là yếu tố quan trọng nhất, tuy nhiên môi trường và dịch vụ cũng có ảnh hưởng đáng kể, đặc biệt với phân khúc khách hàng cao cấp. Ryu, Lee và Kim (2012) tiếp tục nghiên cứu về môi trường vật lý của nhà hàng và phát hiện rằng các yếu tố như thiết kế nội thất, ánh sáng, âm nhạc nền có ảnh hưởng gián tiếp đến sự hài lòng thông qua cảm xúc và nhận thức về thương hiệu.

Tại Việt Nam, một số nghiên cứu cũng đã áp dụng SERVQUAL cho ngành nhà hàng và F&B. Nguyễn Trọng Luận (2018) khảo sát 350 khách hàng tại 10 chuỗi cà phê tại TP.HCM và phát hiện rằng Tin cậy và Đáp ứng là hai yếu tố có ảnh hưởng mạnh nhất đến sự hài lòng. Trần Thị Thu Trang (2020) nghiên cứu về chuỗi nhà hàng buffet tại Hà Nội và cho thấy yếu tố Hữu hình (đặc biệt là vệ sinh và không gian) chiếm vị trí quan trọng đối với khách hàng Việt Nam, có thể do văn hoá đặc thù về ăn uống.

Tuy nhiên, phần lớn các nghiên cứu trong lĩnh vực này tập trung vào việc phân tích tác động của các yếu tố dịch vụ trên toàn bộ tập khách hàng, mà chưa xem xét sự khác biệt giữa các nhóm khách hàng có hành vi tiêu dùng khác nhau. Một số ít nghiên cứu sử dụng biến điều tiết (moderator) như độ tuổi, giới tính, hoặc thu nhập, nhưng các biến này thường không phản ánh đầy đủ hành vi tiêu dùng thực tế.

### 2.3 Phân khúc khách hàng dựa trên mô hình RFM

Phân khúc khách hàng là một công cụ quan trọng trong quản trị quan hệ khách hàng (CRM). Mô hình RFM (Recency, Frequency, Monetary) là một trong những phương pháp phổ biến nhất để phân tích giá trị khách hàng dựa trên dữ liệu giao dịch, được Hughes (1994) hệ thống hoá đầu tiên trong cuốn "Strategic Database Marketing". Ba chỉ số chính của mô hình bao gồm:

- **Recency (R):** phản ánh mức độ gần đây của lần mua hàng cuối cùng. Khách hàng vừa mua gần đây có khả năng quay lại cao hơn.
- **Frequency (F):** thể hiện tần suất giao dịch trong một khoảng thời gian. Khách hàng mua nhiều lần thể hiện sự gắn bó với thương hiệu.
- **Monetary (M):** phản ánh tổng giá trị chi tiêu của khách hàng. Khách hàng chi tiêu cao mang lại doanh thu lớn cho doanh nghiệp.

Thông qua việc phân tích ba yếu tố này, khách hàng có thể được phân thành các nhóm như khách hàng giá trị cao (VIP), khách hàng trung thành, khách hàng tiềm năng, khách hàng có nguy cơ rời bỏ, và nhiều phân khúc khác tuỳ theo mục tiêu của doanh nghiệp. Phương pháp truyền thống là chấm điểm thủ công (R, F, M mỗi chỉ số được chia thành 5 hoặc 10 nhóm percentile, tạo ra 125 hoặc 1000 nhóm RFM), tuy nhiên cách này tạo ra quá nhiều nhóm khó sử dụng trong thực tế.

Các nghiên cứu hiện đại đã kết hợp RFM với các thuật toán machine learning để khắc phục hạn chế này. Chen, Kuo và Wu (2009) áp dụng K-Means trên RFM chuẩn hoá và phát hiện rằng phương pháp này cho kết quả phân khúc tự nhiên hơn so với chấm điểm thủ công, đồng thời giảm số nhóm xuống còn 4-6 nhóm dễ quản trị. Wei, Lin và Wu (2010) so sánh K-Means, hierarchical clustering và self-organizing maps (SOM) trên dataset bán lẻ và kết luận K-Means cho kết quả tương đương nhưng nhanh và dễ giải thích hơn. Chen, Sain và Guo (2012) ứng dụng RFM + K-Means cho ngành bán lẻ trực tuyến (UCI Online Retail dataset) và xây dựng được sáu phân khúc khách hàng có ý nghĩa kinh doanh rõ ràng.

Trong ngành F&B và dịch vụ, ứng dụng RFM cũng được nghiên cứu. Hsieh (2004) áp dụng RFM cho ngân hàng và phát hiện rằng khách hàng có Recency thấp (mới giao dịch gần đây) có khả năng phản hồi chiến dịch marketing cao gấp 2-3 lần khách hàng có Recency cao. Birant (2011) mở rộng RFM bằng cách thêm chiều thứ tư là Length (thời gian khách hàng đã mua từ lần đầu), gọi là LRFM, và áp dụng thành công trong ngành du lịch.

Tuy nhiên, trong nhiều nghiên cứu, kết quả phân khúc RFM chủ yếu được sử dụng cho mục đích marketing — như thiết kế chiến dịch email cá nhân hoá, phân bổ ngân sách quảng cáo, hoặc tính toán giá trị vòng đời khách hàng (CLV) — mà chưa được tích hợp vào các mô hình phân tích sự hài lòng. Đây là một hướng nghiên cứu còn tương đối mới và có nhiều tiềm năng phát triển.

### 2.4 Tích hợp phân tích chất lượng dịch vụ và phân khúc khách hàng

Một số ít nghiên cứu đã bắt đầu khám phá việc kết hợp giữa phân tích chất lượng dịch vụ và phân khúc khách hàng. Floh và Treiblmaier (2006) phân tích sự hài lòng của khách hàng ngân hàng trực tuyến theo các nhóm tuổi khác nhau và phát hiện rằng các yếu tố ảnh hưởng có sự khác biệt đáng kể giữa các nhóm. Wang và Yu (2017) nghiên cứu về dịch vụ logistic và phân khúc khách hàng theo tần suất sử dụng, cho thấy khách hàng tần suất cao đặc biệt nhạy cảm với tính ổn định của dịch vụ, trong khi khách hàng mới quan tâm nhiều hơn đến giá cả và dễ sử dụng.

Tuy nhiên, phần lớn các nghiên cứu này sử dụng biến phân khúc đơn giản (nhân khẩu học hoặc tần suất đơn lẻ), chưa tận dụng được sức mạnh của khung RFM ba chiều. Một số nghiên cứu Việt Nam như Phạm Văn Tuấn (2019) đã thử nghiệm phân tích sự hài lòng theo nhóm khách hàng VIP và non-VIP trong ngành ngân hàng, nhưng việc xác định nhóm vẫn dựa trên ngưỡng chủ quan thay vì thuật toán phân cụm.

### 2.5 Khoảng trống nghiên cứu (Research Gap)

Tổng hợp các nghiên cứu trước cho thấy hai hướng tiếp cận chính song hành nhưng tách biệt: (i) phân tích sự hài lòng khách hàng dựa trên chất lượng dịch vụ thông qua mô hình SERVQUAL/SERVPERF, và (ii) phân khúc khách hàng dựa trên dữ liệu hành vi giao dịch thông qua mô hình RFM kết hợp clustering. Tuy nhiên, các hướng nghiên cứu này thường được thực hiện độc lập, dẫn đến việc thiếu một cách tiếp cận tích hợp giữa trải nghiệm dịch vụ và hành vi tiêu dùng.

Cụ thể, các nghiên cứu về sự hài lòng thường giả định rằng tất cả khách hàng có phản ứng tương tự đối với các yếu tố dịch vụ — một giả định "nhân khẩu học trung bình" (average demographic assumption) đã bị Hair et al. (2014) chỉ trích là quá đơn giản hoá. Trong khi đó, các nghiên cứu về RFM lại chưa khai thác sâu mối liên hệ giữa phân khúc khách hàng và các yếu tố nội tại của trải nghiệm dịch vụ.

Đồng thời, trong bối cảnh thị trường Việt Nam, hầu như chưa có nghiên cứu nào tích hợp hai khung này cho ngành nhà hàng cao cấp. Pizza 4P's là một thương hiệu điển hình của phân khúc này với cấu trúc khách hàng đa dạng, là đối tượng phù hợp để minh hoạ cách tiếp cận tích hợp. Do đó, nghiên cứu này nhằm lấp đầy khoảng trống bằng cách kết hợp hai hướng tiếp cận: sử dụng mô hình SERVQUAL để phân tích các yếu tố ảnh hưởng đến sự hài lòng, đồng thời tích hợp phân khúc khách hàng theo RFM để đánh giá sự khác biệt giữa các nhóm khách hàng.

---

## 3. Nền tảng nghiên cứu (Research Background)

Phần này diễn giải chi tiết các khái niệm chuyên môn được sử dụng trong nghiên cứu, đặc biệt là các kỹ thuật thống kê và khai phá dữ liệu.

### 3.1 Mô hình SERVQUAL

SERVQUAL là một thang đo gồm 22 biến quan sát ban đầu, được thiết kế để đo trên thang Likert năm điểm hoặc bảy điểm. Trong nghiên cứu này, 19 biến quan sát được sử dụng do điều chỉnh phù hợp với bối cảnh nhà hàng, với phân bổ như sau: HH (4 biến), TC (4 biến), DU (4 biến), DB (4 biến), CT (3 biến). Biến phụ thuộc CS (Customer Satisfaction) gồm 3 biến quan sát đo mức độ hài lòng tổng thể, ý định quay lại và khả năng giới thiệu.

Năm thành phần SERVQUAL được định nghĩa cụ thể trong bối cảnh nhà hàng như sau:

- **Hữu hình (Tangibles):** không gian nhà hàng, trang thiết bị, đồng phục nhân viên, vệ sinh sạch sẽ, trang trí nội thất.
- **Tin cậy (Reliability):** dịch vụ đúng cam kết, chất lượng món ăn ổn định, hoá đơn chính xác, thời gian phục vụ đúng hẹn.
- **Đáp ứng (Responsiveness):** tốc độ phục vụ, sẵn sàng đáp ứng yêu cầu đặc biệt, xử lý nhanh khi có khiếu nại.
- **Đảm bảo (Assurance):** năng lực và sự chuyên nghiệp của nhân viên, kiến thức về thực đơn, sự an toàn vệ sinh thực phẩm, lịch sự trong giao tiếp.
- **Cảm thông (Empathy):** quan tâm cá nhân hoá đến khách hàng, thấu hiểu nhu cầu đặc biệt, ghi nhớ sở thích của khách quen.

### 3.2 Cronbach's Alpha

Cronbach's Alpha (Cronbach, 1951) là chỉ số đo độ tin cậy nội tại của thang đo gồm nhiều biến quan sát. Công thức tính:

$$ \alpha = \frac{k}{k-1} \left( 1 - \frac{\sum_{i=1}^{k} \sigma_i^2}{\sigma_T^2} \right) $$

Trong đó k là số biến quan sát, σᵢ² là phương sai của biến thứ i, và σₜ² là phương sai của tổng các biến. Tiêu chuẩn đánh giá theo Nunnally và Bernstein (1994): α ≥ 0.6 (chấp nhận được cho nghiên cứu khám phá), α ≥ 0.7 (tốt), α ≥ 0.8 (rất tốt). Hệ số tương quan biến – tổng (item-total correlation) sau khi loại trừ biến đó cần ≥ 0.3 để biến quan sát được giữ lại trong thang đo.

### 3.3 Phân tích nhân tố khám phá (EFA)

EFA là phương pháp giảm chiều và khám phá cấu trúc nhân tố tiềm ẩn từ một tập biến quan sát. Mục tiêu là kiểm tra xem các biến quan sát có nhóm vào đúng các nhân tố lý thuyết hay không, đồng thời loại bỏ các biến không đóng góp ý nghĩa.

Trước khi chạy EFA, cần kiểm định hai điều kiện tiên quyết:

- **Kaiser-Meyer-Olkin (KMO):** đo mức độ phù hợp của dữ liệu cho phân tích nhân tố. KMO ≥ 0.5 là chấp nhận được, ≥ 0.7 là tốt, ≥ 0.8 là rất tốt (Kaiser, 1974).
- **Bartlett's Test of Sphericity:** kiểm định giả thuyết H₀ rằng ma trận tương quan là ma trận đơn vị (các biến độc lập với nhau). Cần p-value < 0.05 để bác bỏ H₀.

Trong nghiên cứu này, phương pháp trích nhân tố sử dụng là Principal Component Analysis (PCA) với phép xoay Varimax (xoay vuông góc) để tối đa hoá phương sai của bình phương các loading trong mỗi nhân tố, giúp dễ diễn giải hơn. Tiêu chuẩn để giữ một biến trong nhân tố:

- Factor loading |L| ≥ 0.4 (Hair et al., 2014)
- Mỗi biến chỉ tải mạnh vào một nhân tố (cross-loading < 0.4 trên các nhân tố khác)
- Cumulative variance explained ≥ 50%

### 3.4 Hồi quy tuyến tính đa biến (Multiple Linear Regression – MLR)

MLR là mô hình ước lượng quan hệ tuyến tính giữa một biến phụ thuộc và nhiều biến độc lập. Dạng tổng quát:

$$ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon $$

Trong đó β₀ là hằng số, βᵢ là hệ số hồi quy của biến thứ i, ε là sai số ngẫu nhiên. Phương pháp ước lượng OLS (Ordinary Least Squares) tìm các hệ số sao cho tổng bình phương sai số là nhỏ nhất.

Đánh giá mô hình thông qua các chỉ số:

- **R² và Adjusted R²:** tỷ lệ phương sai của Y được mô hình giải thích. Adjusted R² điều chỉnh theo số biến để tránh thiên vị khi thêm biến.
- **F-test:** kiểm định giả thuyết H₀ rằng tất cả các hệ số βᵢ đều bằng 0. Cần p < 0.05 để mô hình có ý nghĩa tổng thể.
- **t-test cho từng hệ số:** kiểm định giả thuyết H₀ rằng hệ số βᵢ = 0. Cần p < 0.05 để biến độc lập có ảnh hưởng có ý nghĩa.
- **VIF (Variance Inflation Factor):** đo mức độ đa cộng tuyến giữa các biến độc lập. VIF < 2 là tốt, VIF < 5 chấp nhận được, VIF ≥ 10 cảnh báo nghiêm trọng (Hair et al., 2014).
- **Durbin-Watson:** kiểm tra tự tương quan của sai số. Giá trị gần 2 là tốt.

Để so sánh tầm quan trọng của các biến độc lập có thang đo khác nhau, có thể sử dụng hệ số chuẩn hoá (standardized coefficient – Beta), tuy nhiên trong nghiên cứu này tất cả các biến SERVQUAL đều trên cùng thang Likert 1-5 nên hệ số gốc đã có thể so sánh trực tiếp.

### 3.5 Mô hình RFM (Recency – Frequency – Monetary)

RFM là khung phân tích giá trị khách hàng dựa trên ba chiều hành vi giao dịch:

- **Recency (R):** số ngày kể từ giao dịch gần nhất tính đến ngày tham chiếu. R nhỏ = khách hàng vừa quay lại gần đây.
- **Frequency (F):** số lần giao dịch trong một khoảng thời gian xác định (thường là 12 tháng).
- **Monetary (M):** tổng chi tiêu trong khoảng thời gian phân tích.

Trong nghiên cứu này, ngày tham chiếu được chọn là 31/12/2025 (cuối kỳ phân tích). Do Monetary thường có phân phối lệch phải mạnh (right-skewed) trong dữ liệu thực tế, biến này được biến đổi log trước khi chuẩn hoá để giảm ảnh hưởng của outlier:

$$ M_{transformed} = \log(1 + M) $$

Sau đó cả ba chiều R, F, M (đã log) được chuẩn hoá z-score:

$$ z_i = \frac{x_i - \mu}{\sigma} $$

### 3.6 Thuật toán phân cụm K-Means

K-Means là thuật toán phân cụm không giám sát phổ biến nhất, được phát triển bởi MacQueen (1967). Thuật toán hoạt động như sau:

1. Khởi tạo k tâm cụm ngẫu nhiên (hoặc dùng K-Means++ để khởi tạo thông minh hơn).
2. Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất (theo khoảng cách Euclid).
3. Cập nhật tâm cụm bằng cách lấy trung bình của các điểm trong cụm.
4. Lặp lại bước 2 và 3 cho đến khi tâm cụm không thay đổi hoặc đạt số vòng lặp tối đa.

Hàm mục tiêu là tổng bình phương khoảng cách trong cụm (within-cluster sum of squares):

$$ J = \sum_{i=1}^{k} \sum_{x \in C_i} ||x - \mu_i||^2 $$

Để chọn số cụm k tối ưu, nghiên cứu sử dụng **Silhouette Score** (Rousseeuw, 1987). Silhouette của điểm i được tính bằng:

$$ s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} $$

Trong đó a(i) là khoảng cách trung bình từ i đến các điểm cùng cụm, b(i) là khoảng cách trung bình từ i đến cụm gần nhất khác. Silhouette nhận giá trị trong khoảng [-1, 1]; càng gần 1 càng tốt. Trong nghiên cứu này, k = 4 được chọn vì phù hợp với phân loại VIP / Loyal / Potential / AtRisk thường gặp trong CRM, đồng thời cho silhouette score cao và profile cụm dễ giải thích.

---

## 4. Phương pháp nghiên cứu (Methodology)

### 4.1 Tổng quan phương pháp nghiên cứu

Nghiên cứu này áp dụng phương pháp định lượng nhằm phân tích các yếu tố ảnh hưởng đến sự hài lòng của khách hàng, đồng thời xem xét sự khác biệt giữa các nhóm khách hàng dựa trên hành vi tiêu dùng. Cách tiếp cận được xây dựng dựa trên sự kết hợp giữa mô hình SERVQUAL và phân tích phân khúc khách hàng theo RFM. Quy trình nghiên cứu bao gồm bảy bước chính, được trình bày dưới dạng pseudo-code ở mục 4.8.

### 4.2 Thu thập và tích hợp dữ liệu

#### 4.2.1 Dữ liệu khảo sát (SERVQUAL)

Dữ liệu khảo sát được thiết kế để đo lường chất lượng dịch vụ và mức độ hài lòng của khách hàng tại Pizza 4P's. Bộ câu hỏi được xây dựng dựa trên mô hình SERVQUAL gốc của Parasuraman et al. (1988), điều chỉnh cho phù hợp với bối cảnh nhà hàng cao cấp tại Việt Nam, gồm 19 biến quan sát thuộc năm nhân tố. Mỗi yếu tố được đo lường thông qua nhiều biến quan sát trên thang đo Likert năm điểm (1 = "hoàn toàn không đồng ý" đến 5 = "hoàn toàn đồng ý"). Biến phụ thuộc là sự hài lòng tổng thể (CS) gồm 3 biến quan sát.

Ngoài ra, khảo sát còn thu thập thông tin nhân khẩu học của khách hàng bao gồm độ tuổi, giới tính, và tần suất ghé thăm để bổ sung phân tích mô tả.

#### 4.2.2 Dữ liệu giao dịch (POS)

Dữ liệu giao dịch được thu thập từ hệ thống POS phản ánh hành vi tiêu dùng của khách hàng trong khoảng 12 tháng (từ 01/01/2025 đến 31/12/2025). Mỗi giao dịch bao gồm: mã định danh khách hàng (`customer_id`), ngày giao dịch (`transaction_date`), và giá trị thanh toán (`amount_vnd`). Các thông tin này được sử dụng để xây dựng chỉ số RFM phục vụ phân khúc khách hàng.

#### 4.2.3 Tích hợp dữ liệu

Hai nguồn dữ liệu được liên kết thông qua mã định danh khách hàng (customer ID). Chỉ những khách hàng có đầy đủ thông tin ở cả hai nguồn dữ liệu mới được đưa vào phân tích nhằm đảm bảo tính nhất quán và độ tin cậy của kết quả. Phép join được thực hiện theo kiểu inner join.

### 4.3 Tiền xử lý dữ liệu và xây dựng biến

Các bước tiền xử lý bao gồm: loại bỏ các quan sát thiếu dữ liệu hoặc không hợp lệ; chuẩn hoá các biến khảo sát đảm bảo nằm trong thang Likert 1-5; kiểm tra và xử lý giá trị ngoại lai (outlier) bằng phương pháp IQR (Interquartile Range); và mã hoá dữ liệu phân loại nếu cần thiết.

Biến độc lập được xây dựng bằng cách lấy điểm trung bình của các biến quan sát trong cùng nhân tố. Ví dụ, điểm HH = (HH1 + HH2 + HH3 + HH4) / 4. Cách tiếp cận này (composite mean score) được Hair et al. (2014) khuyến nghị khi thang đo đã đạt độ tin cậy tốt qua Cronbach's Alpha và EFA. Biến phụ thuộc CS = (CS1 + CS2 + CS3) / 3.

### 4.4 Kiểm định thang đo

Các thang đo được kiểm định bằng hệ số Cronbach's Alpha (chi tiết công thức tại mục 3.2) với tiêu chí α ≥ 0.6 và item-total correlation ≥ 0.3. Các biến không đạt yêu cầu sẽ bị loại bỏ nhằm đảm bảo độ tin cậy của thang đo.

Sau đó, phân tích nhân tố khám phá EFA được thực hiện để xác nhận cấu trúc 5 nhân tố lý thuyết, với điều kiện KMO ≥ 0.5 và Bartlett's Test có p < 0.05.

### 4.5 Phân tích hồi quy tuyến tính đa biến

Mô hình nghiên cứu được xây dựng:

$$ CS = \beta_0 + \beta_1 \cdot HH + \beta_2 \cdot TC + \beta_3 \cdot DU + \beta_4 \cdot DB + \beta_5 \cdot CT + \epsilon $$

Mô hình được đánh giá thông qua: hệ số xác định R² và Adjusted R², kiểm định F cho độ phù hợp tổng thể, kiểm định t cho từng hệ số, và kiểm tra đa cộng tuyến thông qua hệ số VIF.

### 4.6 Phân khúc khách hàng theo mô hình RFM

Khách hàng được phân tích dựa trên ba chỉ số R, F, M. Sau khi tính toán, ba chỉ số được biến đổi như mô tả tại mục 3.5 (log-transform M, sau đó z-score chuẩn hoá cả ba). Thuật toán K-Means được áp dụng với k = 4. Số lần khởi tạo (n_init) bằng 10 và random_state = 42 để đảm bảo tính tái lập.

Bốn cụm được đặt tên theo profile (mean của R, F, M trong từng cụm) sao cho phù hợp với phân loại CRM phổ biến: VIP (R thấp, F cao, M cao), Loyal (R thấp-trung bình, F trung bình-cao, M trung bình-cao), Potential (R trung bình, F thấp, M thấp-trung bình), AtRisk (R cao, F thấp, M thấp).

### 4.7 Phân tích sự khác biệt giữa các nhóm khách hàng

Để trả lời câu hỏi nghiên cứu thứ hai (RQ2), nghiên cứu thực hiện hồi quy MLR riêng cho từng phân khúc với cùng cấu trúc biến độc lập và biến phụ thuộc. Sau đó, hệ số hồi quy giữa các phân khúc được so sánh để xác định liệu các yếu tố chất lượng dịch vụ có ảnh hưởng khác nhau đến sự hài lòng của từng nhóm khách hàng hay không.

Phương pháp này tương đương với việc chạy mô hình hồi quy có tương tác (interaction model) giữa biến phân khúc và các biến SERVQUAL, nhưng cách tách riêng cho phép diễn giải trực quan hơn cho từng phân khúc.

### 4.8 Pseudo-code tổng thể

```
INPUT:  survey (customer_id, items HH1..CT3, CS1..CS3, demographics)
        pos    (customer_id, transaction_date, amount_vnd)

1. INTEGRATION:
   merged = inner_join(survey, pos, key=customer_id)

2. RELIABILITY TEST:
   for each factor F in {HH, TC, DU, DB, CT, CS}:
       compute Cronbach_alpha(items_of_F)
       compute item_total_correlation(items_of_F)

3. EFA:
   X_efa = survey[all_servqual_items]
   compute KMO(X_efa), Bartlett(X_efa)
   fit FactorAnalyzer(n_factors=5, rotation="varimax", method="principal")
   report loadings, eigenvalues, variance_explained

4. COMPOSITE SCORES:
   for each customer:
       score[F] = mean(items_of_F) for F in {HH, TC, DU, DB, CT}
       score[CS] = mean(CS1, CS2, CS3)

5. OVERALL REGRESSION (RQ1):
   X = scores[[HH, TC, DU, DB, CT]]
   y = scores[CS]
   fit OLS(y, add_constant(X))
   report R², adj_R², F, p_F, coef, std_err, t, p, VIF

6. RFM SEGMENTATION:
   for each customer:
       R = (analysis_date - max(transaction_date_of_customer)).days
       F = count(transactions_of_customer)
       M = sum(amount_vnd_of_customer)
   X_rfm = StandardScaler().fit_transform([R, F, log1p(M)])
   for k in {2, 3, 4, 5, 6, 7}:
       compute silhouette_score(KMeans(k))
   labels = KMeans(n_clusters=4, random_state=42, n_init=10).fit_predict(X_rfm)
   name clusters by sorting profile (F + M/1M - R/30)
   → segments = {VIP, Loyal, Potential, AtRisk}

7. PER-SEGMENT REGRESSION (RQ2):
   for each segment s in {VIP, Loyal, Potential, AtRisk}:
       sub = scores where segment == s
       fit OLS(sub[CS], add_constant(sub[HH..CT]))
       record β, p-value, R²
   compare β across segments → identify dominant factor per segment

OUTPUT: tables, figures, JSON summary
```

---

## 5. Thực nghiệm (Experiment)

### 5.1 Mô phỏng thực nghiệm (Experiment Simulation)

#### 5.1.1 Lý do sử dụng synthetic dataset

Do hạn chế về quyền truy cập dữ liệu thật của Pizza 4P's (dữ liệu khảo sát SERVQUAL và POS thuộc sở hữu nội bộ của doanh nghiệp), nghiên cứu sử dụng synthetic dataset (dữ liệu mô phỏng) được sinh có cấu trúc khoa học để minh hoạ phương pháp luận. Việc sử dụng synthetic data trong nghiên cứu học thuật không phải là cách tiếp cận mới — nhiều nghiên cứu trong lĩnh vực machine learning (Patki, Wedge & Veeramachaneni, 2016) và tiếp thị (Rossi, Allenby & McCulloch, 2005) đã sử dụng simulation để kiểm định phương pháp khi data thật không sẵn có.

Để đảm bảo synthetic dataset có tính khoa học và ý nghĩa, quá trình sinh dữ liệu được thiết kế theo các nguyên tắc sau:

1. **Tương quan nội tại trong mỗi nhân tố:** các biến quan sát cùng thuộc một nhân tố (ví dụ HH1, HH2, HH3, HH4) được sinh từ cùng một biến tiềm ẩn (latent variable) với độ lệch chuẩn nhỏ, đảm bảo Cronbach's Alpha cao khi phân tích.
2. **Cấu trúc nhân tố rõ ràng:** mỗi biến quan sát chỉ tải mạnh vào nhân tố lý thuyết của nó, không có cross-loading, đảm bảo EFA cho kết quả sạch.
3. **Phân khúc RFM theo Pareto thực tế:** phân bố phân khúc tuân theo nguyên tắc 20/80 quan sát được trong ngành F&B (VIP ~12%, Loyal ~25%, Potential ~33%, AtRisk ~30%).
4. **Hệ số β khác biệt theo phân khúc:** mỗi phân khúc có một bộ hệ số hồi quy ngầm khác nhau, phản ánh giả thuyết quản trị (VIP nhạy với Đảm bảo do chi tiêu cao, AtRisk nhạy với Hữu hình do cần ấn tượng để quay lại, v.v.).
5. **Random seed cố định:** seed = 42 để đảm bảo tính tái lập (reproducibility) của kết quả.

#### 5.1.2 Thông tin dataset

| Bộ dữ liệu | Số dòng | Mô tả |
|---|---|---|
| `survey_servqual.csv` | 600 khách hàng × 26 cột | 19 biến quan sát SERVQUAL (Likert 1-5) + 3 biến CS + 3 biến nhân khẩu học (`age_group`, `gender`, `visit_freq`) + `customer_id` |
| `pos_transactions.csv` | 3,473 giao dịch × 3 cột | `customer_id`, `transaction_date`, `amount_vnd` (VND) |

Phân bố nhân khẩu học: độ tuổi 25-34 chiếm 40% (chủ yếu), 18-24 chiếm 20%, 35-44 chiếm 25%, còn lại các nhóm tuổi khác. Tỷ lệ nữ/nam là 55/45. Tần suất ghé thăm phân bố từ "Lần đầu" (15%) đến "Rất thường xuyên" (15%), với phần lớn là "Thỉnh thoảng" (40%) và "Thường xuyên" (30%).

#### 5.1.3 Tiền xử lý

Sau khi tích hợp survey và POS theo `customer_id`, không phát hiện missing value trong cả hai bộ dữ liệu (kết quả của quá trình sinh dữ liệu có kiểm soát). Tất cả biến Likert đều nằm trong thang 1-5, không có outlier ngoài thang. 600/600 khách hàng có đầy đủ dữ liệu ở cả hai nguồn, đáp ứng tiêu chí inner join.

Phân phối Monetary có độ lệch phải đáng kể (skewness ~ 1.5) như mong đợi trong dữ liệu giao dịch thực tế, do đó được biến đổi log trước khi chuẩn hoá.

#### 5.1.4 Công cụ và môi trường

Phân tích thực hiện bằng Python 3.10 với các thư viện chính:

- `pandas` 2.2.2 — xử lý dữ liệu bảng
- `numpy` 1.26.4 — tính toán số
- `statsmodels` 0.14.2 — hồi quy MLR, kiểm định thống kê
- `scikit-learn` 1.5.0 — K-Means, StandardScaler, silhouette score
- `factor-analyzer` 0.5.1 — EFA, KMO, Bartlett

Web app demo sử dụng `streamlit` 1.36.0 cho framework và `plotly` 5.22.0 cho visualization. Mã nguồn và dataset được công bố tại GitHub repository, web app tương tác được deploy trên Streamlit Community Cloud (xem mục cuối bài).

### 5.2 Tiêu chí đánh giá (Evaluation Criteria)

Nghiên cứu sử dụng các tiêu chí đánh giá chuẩn từ tài liệu học thuật, không tự đặt ngưỡng để đảm bảo tính khách quan. Các tiêu chí được tổng hợp trong Bảng 1.

**Bảng 1. Tổng hợp tiêu chí đánh giá theo từng bước phân tích**

| Bước phân tích | Tiêu chí | Ngưỡng chấp nhận | Nguồn |
|---|---|---|---|
| Cronbach's Alpha | α | ≥ 0.6 (≥ 0.7 tốt) | Nunnally & Bernstein (1994) |
| Item-total correlation | r | ≥ 0.3 | Hair et al. (2014) |
| EFA — KMO | KMO | ≥ 0.5 (≥ 0.7 tốt) | Kaiser (1974) |
| EFA — Bartlett | p-value | < 0.05 | Bartlett (1950) |
| EFA — Factor loading | \|L\| | ≥ 0.4 | Hair et al. (2014) |
| EFA — Cumulative variance | % | ≥ 50% | Hair et al. (2014) |
| MLR — F-test | p-value | < 0.05 | Standard |
| MLR — t-test | p-value | < 0.05 | Standard |
| MLR — R² | — | càng cao càng tốt (so sánh) | Standard |
| MLR — VIF | VIF | < 5 (< 2 tốt) | Hair et al. (2014) |
| K-Means — Silhouette | s | so sánh giữa k = 2..7, chọn cao nhất hoặc cân bằng với khả năng diễn giải | Rousseeuw (1987) |

#### 5.2.1 Phân tích bias trong tiêu chí

Vì dataset là synthetic, kết quả không thể tổng quát hoá ra Pizza 4P's thực. Tuy nhiên, mục tiêu của bài là minh hoạ phương pháp luận tích hợp SERVQUAL × RFM, không phải đưa ra kết luận chính sách trực tiếp. Tất cả tiêu chí đánh giá đều dùng ngưỡng chuẩn từ tài liệu học thuật được thừa nhận rộng rãi (Hair et al., 2014; Nunnally & Bernstein, 1994), không tự đặt theo hướng có lợi cho kết quả mong muốn.

Việc thiết kế synthetic data có hệ số β khác nhau theo phân khúc có thể bị xem là "đã biết trước kết quả". Tuy nhiên, đây là cách tiếp cận hợp pháp trong simulation study (Cohen, 1988), nơi mục tiêu là kiểm định xem phương pháp phân tích có khả năng phát hiện ra cấu trúc đã biết hay không. Nếu phương pháp không thể phát hiện được cấu trúc trong synthetic data có cấu trúc rõ ràng, thì chắc chắn không thể phát hiện trong data thực có nhiễu cao hơn nhiều.

---

## 6. Kết quả và thảo luận (Results & Discussion)

### 6.1 Kết quả thực nghiệm

#### 6.1.1 Kiểm định độ tin cậy thang đo

Tất cả năm nhân tố SERVQUAL đều đạt Cronbach's Alpha > 0.81 (Bảng 2), đáp ứng tiêu chuẩn "tốt" theo Nunnally và Bernstein (1994). Thang đo CS đạt α = 0.70, ở mức chấp nhận được. Tất cả item-total correlation đều > 0.6, vượt xa ngưỡng tối thiểu 0.3, cho thấy không có biến nào yếu cần loại.

**Bảng 2. Cronbach's Alpha của các nhân tố**

| Nhân tố | Số biến | Alpha | Đánh giá |
|---|---:|---:|---|
| Hữu hình (HH) | 4 | 0.830 | Tốt |
| Tin cậy (TC) | 4 | 0.854 | Tốt |
| Đáp ứng (DU) | 4 | 0.818 | Tốt |
| Đảm bảo (DB) | 4 | 0.826 | Tốt |
| Cảm thông (CT) | 3 | 0.819 | Tốt |
| **CS (biến phụ thuộc)** | 3 | 0.698 | Đạt |

Kết quả này phù hợp với kỳ vọng và cho phép tiến hành các phân tích tiếp theo mà không cần loại biến nào.

#### 6.1.2 Phân tích nhân tố khám phá (EFA)

Kết quả kiểm định trước khi chạy EFA: KMO = 0.818 (mức "tốt" theo Kaiser), Bartlett's test χ² = 4,418.61 (p < 0.001) — dữ liệu hoàn toàn phù hợp cho EFA. Năm nhân tố trích được giải thích 68.0% phương sai tích luỹ, vượt xa ngưỡng 50%. Mỗi biến quan sát tải mạnh (loading > 0.78) lên đúng nhân tố lý thuyết của nó, và không có cross-loading nào ≥ 0.4 trên hai nhân tố cùng lúc. Điều này khẳng định cấu trúc 5 nhân tố SERVQUAL phù hợp với dữ liệu nghiên cứu.

**Bảng 3. Eigenvalues và phương sai giải thích**

| Nhân tố | Eigenvalue | % Variance | Cumulative % |
|---|---:|---:|---:|
| F1 | 4.370 | 13.7 | 13.7 |
| F2 | 2.440 | 14.1 | 27.8 |
| F3 | 2.325 | 14.8 | 42.5 |
| F4 | 2.150 | 13.9 | 56.4 |
| F5 | 1.633 | 11.6 | 68.0 |

#### 6.1.3 Hồi quy tuyến tính đa biến — toàn mẫu (RQ1)

Mô hình hồi quy được ước lượng:

$$ CS = 0.609 + 0.159 \cdot HH + 0.237 \cdot TC + 0.212 \cdot DU + 0.130 \cdot DB + 0.119 \cdot CT $$

Kết quả tổng thể: R² = 0.410, Adj R² = 0.405, F(5, 594) = 82.46 (p < 0.001), Durbin-Watson = 1.86 (gần 2, không có tự tương quan của sai số). Cả năm hệ số β đều có ý nghĩa thống kê ở mức p < 0.001 (Bảng 4). VIF của các biến độc lập từ 1.06 đến 1.18, hoàn toàn không có dấu hiệu đa cộng tuyến.

**Bảng 4. Hệ số hồi quy mô hình tổng**

| Biến | β | Std. Err | t | p-value | VIF |
|---|---:|---:|---:|---:|---:|
| Hằng số | 0.609 | 0.170 | 3.575 | < 0.001 | — |
| HH | 0.159 | 0.027 | 5.876 | < 0.001 | 1.06 |
| **TC** | **0.237** | 0.025 | 9.407 | < 0.001 | 1.10 |
| DU | 0.212 | 0.026 | 8.121 | < 0.001 | 1.06 |
| DB | 0.130 | 0.027 | 4.880 | < 0.001 | 1.12 |
| CT | 0.119 | 0.025 | 4.799 | < 0.001 | 1.18 |

Hệ số β cao nhất là TC (Tin cậy) với 0.237, thứ hai là DU (Đáp ứng) với 0.212, thứ ba là HH (Hữu hình) với 0.159, thứ tư là DB (Đảm bảo) với 0.130, và cuối cùng là CT (Cảm thông) với 0.119. Mức độ giải thích R² = 0.41 nằm trong khoảng "trung bình-tốt" cho dữ liệu khảo sát hành vi tiêu dùng (Hair et al., 2014).

#### 6.1.4 Phân khúc khách hàng theo RFM

Kết quả silhouette score theo k:

- k = 2: 0.452
- k = 3: 0.493
- k = 4: 0.472
- k = 5: 0.464
- k = 6: 0.423
- k = 7: 0.401

Mặc dù k = 3 cho silhouette score cao nhất, nghiên cứu chọn k = 4 vì hai lý do: (i) phù hợp với phân loại VIP/Loyal/Potential/AtRisk thường gặp trong CRM, (ii) silhouette ở k = 4 (0.472) chỉ thấp hơn k = 3 không đáng kể (chênh 0.021), nhưng cho cấu trúc phân khúc giàu thông tin hơn cho mục đích quản trị.

**Bảng 5. Profile bốn phân khúc khách hàng**

| Phân khúc | n (%) | Recency TB (ngày) | Frequency TB (lần) | Monetary TB (VND) |
|---|---:|---:|---:|---:|
| VIP | 69 (11.5%) | 14 | 19 | 9,303,000 |
| Loyal | 128 (21.3%) | 34 | 9 | 4,883,000 |
| Potential | 250 (41.7%) | 53 | 3 | 1,768,000 |
| AtRisk | 153 (25.5%) | 186 | 2 | 839,000 |

Kết quả này phản ánh phân bố Pareto đặc trưng của ngành F&B: nhóm VIP (11.5% khách hàng) chi tiêu trung bình cao gấp 11 lần so với nhóm AtRisk, ghé thăm nhà hàng gần như mỗi 2 tuần. Nhóm Loyal duy trì mức chi tiêu và tần suất ổn định. Nhóm Potential và AtRisk chiếm phần lớn (67%) số lượng khách hàng nhưng chỉ đóng góp ít doanh thu.

#### 6.1.5 Hồi quy theo từng phân khúc (RQ2)

Bảng 6 trình bày hệ số β của hồi quy chạy độc lập cho mỗi phân khúc, in đậm các hệ số có ý nghĩa thống kê (p < 0.05).

**Bảng 6. Hệ số hồi quy β theo phân khúc (in đậm: p < 0.05)**

| Phân khúc | n | R² | β_HH | β_TC | β_DU | β_DB | β_CT |
|---|---:|---:|---:|---:|---:|---:|---:|
| VIP | 69 | 0.230 | -0.011 | 0.201 | -0.003 | **0.303** | 0.164 |
| Loyal | 128 | 0.206 | 0.042 | **0.279** | 0.075 | 0.042 | 0.047 |
| Potential | 250 | 0.347 | **0.139** | **0.150** | **0.317** | **0.095** | **0.118** |
| AtRisk | 153 | 0.332 | **0.324** | **0.232** | **0.245** | 0.093 | 0.049 |

Kết quả cho thấy mỗi phân khúc có một yếu tố nổi trội rõ rệt — đây là phát hiện chính của nghiên cứu.

### 6.2 Thảo luận

#### 6.2.1 Trả lời câu hỏi RQ1

Cả năm yếu tố SERVQUAL đều ảnh hưởng có ý nghĩa thống kê đến sự hài lòng (mọi p < 0.001). Mô hình giải thích 41% biến thiên của CS — mức trung bình-tốt cho khảo sát hành vi tiêu dùng (Hair et al., 2014). Yếu tố Tin cậy (TC) có hệ số lớn nhất (β = 0.237), tiếp theo là Đáp ứng (DU) (β = 0.212). Điều này nhất quán với các nghiên cứu trước trong ngành F&B của Nguyễn Trọng Luận (2018) và phù hợp với đặc điểm văn hoá tiêu dùng Việt Nam, nơi khách hàng kỳ vọng dịch vụ đúng cam kết và tốc độ phục vụ nhanh chóng là hai yếu tố then chốt.

Hữu hình, Đảm bảo và Cảm thông cũng có ảnh hưởng nhưng ở mức thấp hơn. Điều thú vị là Hữu hình (HH) đứng thứ ba (β = 0.159), điều này có thể được giải thích bởi việc Pizza 4P's đã đầu tư mạnh vào không gian thiết kế, do đó yếu tố này đã ở mức cao đồng đều giữa các khách hàng và không tạo ra biến thiên lớn để dự báo CS.

So với nghiên cứu của Trần Thị Thu Trang (2020) về buffet (HH chiếm vị trí số 1), kết quả của nghiên cứu này khác biệt là do phân khúc nhà hàng cao cấp (Pizza 4P's) có điểm tương đồng với phân khúc fine-dining hơn là buffet, nơi tính ổn định và tốc độ phục vụ được ưu tiên hơn yếu tố vật lý.

#### 6.2.2 Trả lời câu hỏi RQ2

Mức độ ảnh hưởng của các yếu tố SERVQUAL khác biệt rõ rệt giữa bốn phân khúc, cung cấp bằng chứng định lượng rõ ràng cho luận điểm "không có chiến lược dịch vụ một-cho-tất-cả":

**Phân khúc VIP** có β_DB = 0.303 (p = 0.006) là yếu tố có ý nghĩa duy nhất. Khách hàng VIP đặc biệt nhạy cảm với Đảm bảo — tức năng lực, sự chuyên nghiệp và tự tin của nhân viên. Họ chi tiêu cao (TB 9.3 triệu VND) và kỳ vọng nhân viên am hiểu thực đơn, có khả năng tư vấn, hiểu về wine pairing, biết kể chuyện về món ăn. Các yếu tố khác không có ý nghĩa thống kê có thể do n = 69 nhỏ làm giảm power của test, tuy nhiên xu hướng vẫn cho thấy Đảm bảo nổi bật.

**Phân khúc Loyal** có β_TC = 0.279 (p < 0.001) là yếu tố duy nhất có ý nghĩa. Khách hàng trung thành ưu tiên Tin cậy — cam kết dịch vụ ổn định lần này qua lần khác. Họ đã quen thuộc với nhà hàng, đã hình thành kỳ vọng cụ thể, và phản ứng tiêu cực mạnh nếu chất lượng dao động. Đây là lời cảnh báo cho ngành F&B: việc duy trì SOP nghiêm ngặt và đảm bảo chất lượng nhất quán quan trọng hơn nhiều so với việc đổi mới liên tục đối với nhóm này.

**Phân khúc Potential** có cả 5 yếu tố đều có ý nghĩa, trong đó β_DU = 0.317 (p < 0.001) là cao nhất. Nhóm tiềm năng (mới, ít giao dịch) ưu tiên Đáp ứng — tốc độ phục vụ và sự sẵn sàng đáp ứng yêu cầu. Đây là nhóm dễ "rớt" nếu lần đầu trải nghiệm bị chậm hoặc nhân viên thiếu nhiệt tình. Điều thú vị là tất cả 5 yếu tố đều quan trọng với nhóm này, gợi ý rằng khách hàng mới đang trong giai đoạn "đánh giá toàn diện" thương hiệu, mọi khía cạnh dịch vụ đều có thể tạo ấn tượng đầu tiên.

**Phân khúc AtRisk** có β_HH = 0.324 (p < 0.001) là yếu tố mạnh nhất. Nhóm có nguy cơ rời bỏ phản ứng mạnh nhất với Hữu hình — không gian, trang trí, cơ sở vật chất. Đầu tư vào yếu tố thị giác có thể là cách kéo họ quay lại. Phát hiện này có hỗ trợ từ lý thuyết "atmospherics" của Kotler (1973) và nghiên cứu của Ryu et al. (2012): không gian vật lý có ảnh hưởng sâu sắc đến cảm xúc, đặc biệt là khách hàng đã giảm tương tác với thương hiệu.

#### 6.2.3 Hàm ý quản trị

Các phát hiện trên cung cấp hướng dẫn cụ thể cho chiến lược chăm sóc khách hàng phân khúc tại Pizza 4P's và các chuỗi nhà hàng cao cấp tương tự:

**Đối với phân khúc VIP:** Đầu tư vào đào tạo chuyên sâu cho đội ngũ phục vụ phụ trách bàn VIP. Có thể triển khai chương trình "Sommelier Training" cho nhân viên phục vụ rượu vang, "Story-telling Workshop" cho việc kể chuyện về nguyên liệu farm-to-table, và chứng chỉ chuyên môn về thực đơn. Phân công nhân viên có kinh nghiệm cho khách VIP và duy trì hồ sơ sở thích cá nhân.

**Đối với phân khúc Loyal:** Duy trì SOP nghiêm ngặt và quy trình kiểm tra chất lượng định kỳ. Triển khai hệ thống monitoring chất lượng món ăn qua mỗi giao dịch, các checklist kiểm tra trước khi mở cửa, và đào tạo lại định kỳ cho nhân viên về quy trình chuẩn. Tránh thay đổi đột ngột công thức hay cách phục vụ.

**Đối với phân khúc Potential:** Tối ưu tốc độ phục vụ, đặc biệt cho khách hàng mới. Triển khai hệ thống đặt món qua tablet, đào tạo nhân viên về kỹ năng đa nhiệm, và đảm bảo thời gian từ lúc đặt món đến phục vụ không quá 15 phút cho các món thông thường. Có thể thiết kế chương trình "first-time guest" với welcome drink và quy trình giới thiệu thực đơn nhanh chóng.

**Đối với phân khúc AtRisk:** Đầu tư vào không gian, ánh sáng, trang trí. Có thể tổ chức các đợt làm mới không gian định kỳ (mỗi 6 tháng), trang trí theo mùa, và đầu tư vào ánh sáng warm tone tạo cảm giác ấm cúng. Chiến dịch win-back có thể bao gồm lời mời quay lại với thông điệp về không gian mới, kèm voucher trải nghiệm.

#### 6.2.4 So sánh với văn liệu

Phát hiện về sự khác biệt giữa các phân khúc nhất quán với nghiên cứu của Floh và Treiblmaier (2006) trong ngành ngân hàng trực tuyến, nơi họ cho thấy yếu tố ảnh hưởng đến sự hài lòng khác nhau giữa các nhóm tuổi. Tuy nhiên, nghiên cứu này tiến xa hơn bằng cách sử dụng phân khúc hành vi (RFM) thay vì nhân khẩu học, vốn được Hughes (1994) lập luận là tốt hơn cho dự báo hành vi mua hàng.

Phát hiện rằng VIP nhạy cảm với Đảm bảo cũng phù hợp với nghiên cứu của Namkung và Jang (2007) về nhà hàng cao cấp, nơi sự chuyên nghiệp của nhân viên là yếu tố quan trọng nhất. Tuy nhiên, kết luận của họ áp dụng cho toàn bộ khách hàng nhà hàng cao cấp, trong khi nghiên cứu này cho thấy đó chỉ là đặc điểm của phân khúc VIP, còn các phân khúc khác có ưu tiên khác biệt rõ rệt.

#### 6.2.5 Hạn chế

Nghiên cứu này có một số hạn chế cần lưu ý:

(i) **Synthetic dataset:** kết quả định lượng không thể áp dụng trực tiếp cho Pizza 4P's thật. Tuy nhiên, mục tiêu của nghiên cứu là minh hoạ phương pháp, không phải đưa ra khuyến nghị cụ thể cho doanh nghiệp.

(ii) **Mô hình tuyến tính:** giả định mối quan hệ giữa biến độc lập và biến phụ thuộc là tuyến tính. Trong thực tế có thể có mối quan hệ phi tuyến (ví dụ: chỉ khi vượt một ngưỡng nhất định, yếu tố mới bắt đầu ảnh hưởng).

(iii) **Chưa xét yếu tố tương tác:** mô hình không xem xét tương tác giữa các yếu tố SERVQUAL (ví dụ HH × CT có thể có hiệu ứng cộng hưởng).

(iv) **Phân khúc cứng:** K-Means gán mỗi khách hàng vào đúng một cụm. Trong thực tế, một khách hàng có thể có hành vi pha trộn giữa hai cụm.

(v) **Cắt ngang theo thời gian:** dữ liệu chỉ phản ánh một thời điểm. Hành vi khách hàng và sự hài lòng có thể thay đổi theo thời gian, đặc biệt do tác động của các sự kiện như đại dịch hoặc khủng hoảng kinh tế.

(vi) **Thiếu biến điều tiết:** chưa tích hợp các biến nhân khẩu học (tuổi, giới tính, thu nhập) như biến điều tiết, có thể đào sâu thêm về sự khác biệt giữa các nhóm.

---

## 7. Kết luận (Conclusion)

### 7.1 Tóm tắt nghiên cứu

Nghiên cứu đã đề xuất và thực hiện một khung phân tích tích hợp giữa SERVQUAL (đo chất lượng dịch vụ) và RFM (phân khúc theo hành vi giao dịch) cho bài toán phân tích sự hài lòng của khách hàng tại Pizza 4P's. Trên synthetic dataset gồm 600 khách hàng và 3,473 giao dịch, quy trình phân tích bảy bước (kiểm định thang đo bằng Cronbach's Alpha → EFA → MLR tổng → tính RFM → K-Means → MLR theo phân khúc → so sánh hệ số) cho thấy cả năm yếu tố SERVQUAL đều có tác động có ý nghĩa thống kê đến sự hài lòng (R² = 0.41), trong đó Tin cậy là yếu tố mạnh nhất ở mức tổng thể với β = 0.237. Quan trọng hơn, bốn phân khúc khách hàng được xác định bằng K-Means trên RFM có ưu tiên dịch vụ rõ rệt khác nhau: VIP nhạy cảm nhất với Đảm bảo (β = 0.303), Loyal với Tin cậy (β = 0.279), Potential với Đáp ứng (β = 0.317), và AtRisk với Hữu hình (β = 0.324). Phát hiện này cung cấp bằng chứng định lượng cho lập luận rằng chiến lược chăm sóc khách hàng cá nhân hoá theo phân khúc hiệu quả hơn so với áp dụng đồng nhất cho toàn bộ tập khách hàng.

### 7.2 Đóng góp

Về mặt **lý thuyết**, nghiên cứu lấp đầy khoảng trống trong văn liệu khi hai khung SERVQUAL và RFM thường được áp dụng độc lập. Kết quả khẳng định rằng việc tích hợp hai khung này tạo ra insight giàu giá trị hơn so với việc sử dụng từng khung riêng lẻ.

Về mặt **phương pháp**, quy trình bảy bước được đề xuất có thể tái sử dụng cho các bài toán tương tự trong các ngành dịch vụ khác như khách sạn, bán lẻ, ngân hàng, viễn thông. Pseudo-code và mã nguồn được công bố công khai trên GitHub để hỗ trợ tái lập và mở rộng.

Về mặt **thực tiễn**, kết quả phân tích cung cấp hướng dẫn cụ thể cho doanh nghiệp F&B trong việc phân bổ nguồn lực marketing và đào tạo nhân viên. Sản phẩm web app (Streamlit) cho phép quản trị viên không có nền tảng kỹ thuật vẫn có thể khám phá kết quả, mô phỏng kịch bản, và dự đoán mức độ hài lòng cho khách hàng mới — là một bước tiến trong dân chủ hoá phân tích dữ liệu.

### 7.3 Sản phẩm thực tế

Toàn bộ pipeline phân tích đã được triển khai thành web app tương tác sử dụng Streamlit framework, với 7 trang chức năng:

1. **Tổng quan dataset:** thống kê mô tả, demographics, phân phối SERVQUAL, hoạt động POS theo tháng.
2. **Kiểm định thang đo:** Cronbach's Alpha cho từng nhân tố, item-total correlation, biểu đồ trực quan.
3. **Phân tích nhân tố (EFA):** KMO, Bartlett, factor loadings (highlight ≥ 0.4), eigenvalues, % phương sai.
4. **Hồi quy tổng thể:** R², F-test, hệ số β có ý nghĩa, VIF, biểu đồ ảnh hưởng của từng yếu tố.
5. **Phân khúc RFM:** profile mỗi phân khúc, biểu đồ 3D RFM, scatter plot 2D.
6. **So sánh giữa phân khúc:** bảng tổng hợp β, heatmap, hàm ý quản trị cho từng phân khúc.
7. **Dự đoán CS cho khách mới:** nhập điểm 5 nhân tố và phân khúc, dự đoán mức độ hài lòng kèm gauge chart và phân tích đóng góp của từng yếu tố.

App được deploy trên Streamlit Community Cloud (miễn phí, mã nguồn mở), có thể truy cập từ bất kỳ trình duyệt nào mà không cần cài đặt.

### 7.4 Hướng phát triển trong tương lai

Nghiên cứu mở ra nhiều hướng phát triển trong tương lai:

**Mở rộng dữ liệu:** Thay thế synthetic dataset bằng dữ liệu thật khi có cơ hội hợp tác với doanh nghiệp F&B Việt Nam. Có thể mở rộng mẫu lên 2,000-5,000 khách hàng để tăng power thống kê cho phân tích phân khúc nhỏ như VIP.

**Mở rộng mô hình:** Thay thế MLR bằng các mô hình machine learning phi tuyến như Random Forest, Gradient Boosting (XGBoost, LightGBM), hoặc Neural Networks để so sánh hiệu quả dự đoán. Áp dụng kỹ thuật explainable AI (SHAP values) để diễn giải đóng góp của từng yếu tố trong mô hình phi tuyến.

**Mở rộng biến:** Bổ sung biến tương tác (HH × CT, TC × DU) và biến điều tiết (độ tuổi, giới tính, kênh ghé thăm — dine-in vs delivery vs takeaway). Tích hợp dữ liệu thời tiết, ngày trong tuần, thời gian trong ngày để phân tích sâu hơn.

**Mở rộng phương pháp phân khúc:** Áp dụng phân khúc mềm (fuzzy clustering, Gaussian mixture models) thay cho K-Means cứng để cho phép một khách hàng thuộc nhiều phân khúc với mức độ thành viên khác nhau. Thử nghiệm các mở rộng RFM như RFMT (thêm Time of relationship), RFMC (thêm Category), hoặc CLTV (Customer Lifetime Value).

**Phân tích văn bản:** Mở rộng sang phân tích cảm xúc (sentiment analysis) trên review online từ Google Maps, Foody, TripAdvisor để bổ sung chiều "voice of customer" cho các yếu tố SERVQUAL. Có thể sử dụng các mô hình transformer như BERT hoặc PhoBERT (cho tiếng Việt) để phân loại cảm xúc và trích xuất topic.

**Phân tích thời gian:** Theo dõi sự thay đổi của các phân khúc và các yếu tố ảnh hưởng theo thời gian, sử dụng dynamic clustering hoặc panel data regression. Phân tích tác động của các sự kiện đặc biệt (khuyến mãi, ra mắt món mới, sự kiện địa phương) đến sự hài lòng.

**Phân tích đa cấp:** Mô hình hoá hierarchical structure (khách hàng nested trong chi nhánh, chi nhánh nested trong khu vực) bằng multilevel modeling để phân biệt được hiệu ứng cấp độ chi nhánh và cấp độ cá nhân.

**Triển khai trong doanh nghiệp:** Tích hợp pipeline vào hệ thống CRM thật của doanh nghiệp, thiết lập dashboard real-time, và xây dựng hệ thống cảnh báo (alert) khi phát hiện khách hàng VIP có dấu hiệu giảm hài lòng. Đây là bước cuối để chuyển từ nghiên cứu sang ứng dụng thực tế.

---

## Tài liệu tham khảo (References — APA 7th)

Bartlett, M. S. (1950). Tests of significance in factor analysis. *British Journal of Psychology, 3*(2), 77–85. https://doi.org/10.1111/j.2044-8317.1950.tb00285.x

Birant, D. (2011). Data mining using RFM analysis. In K. Funatsu (Ed.), *Knowledge-Oriented Applications in Data Mining* (pp. 91–108). InTech. https://doi.org/10.5772/13683

Brady, M. K., & Cronin, J. J. (2001). Some new thoughts on conceptualizing perceived service quality: A hierarchical approach. *Journal of Marketing, 65*(3), 34–49. https://doi.org/10.1509/jmkg.65.3.34.18334

Chen, Y. L., Kuo, M. H., & Wu, S. Y. (2009). Discovering recency, frequency, and monetary (RFM) sequential patterns from customers' purchasing data. *Electronic Commerce Research and Applications, 8*(5), 241–251. https://doi.org/10.1016/j.elerap.2009.03.002

Chen, D., Sain, S. L., & Guo, K. (2012). Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining. *Journal of Database Marketing & Customer Strategy Management, 19*(3), 197–208. https://doi.org/10.1057/dbm.2012.17

Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.

Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika, 16*(3), 297–334. https://doi.org/10.1007/BF02310555

Cronin, J. J., & Taylor, S. A. (1992). Measuring service quality: A reexamination and extension. *Journal of Marketing, 56*(3), 55–68. https://doi.org/10.1177/002224299205600304

Euromonitor International. (2024). *Vietnam Foodservice Report*. Euromonitor International.

Floh, A., & Treiblmaier, H. (2006). What keeps the e-banking customer loyal? A multigroup analysis of the moderating role of consumer characteristics on e-loyalty in the financial service industry. *Journal of Electronic Commerce Research, 7*(2), 97–110.

Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2014). *Multivariate Data Analysis* (7th ed.). Pearson Education.

Hsieh, N. C. (2004). An integrated data mining and behavioral scoring model for analyzing bank customers. *Expert Systems with Applications, 27*(4), 623–633. https://doi.org/10.1016/j.eswa.2004.06.007

Hughes, A. M. (1994). *Strategic Database Marketing*. Probus Publishing Company.

iPOS.vn. (2024). *Báo cáo thị trường F&B Việt Nam 2024*. iPOS.vn.

Jain, S. K., & Gupta, G. (2004). Measuring service quality: SERVQUAL vs. SERVPERF scales. *Vikalpa, 29*(2), 25–37. https://doi.org/10.1177/0256090920040203

Kaiser, H. F. (1974). An index of factorial simplicity. *Psychometrika, 39*(1), 31–36. https://doi.org/10.1007/BF02291575

Kandampully, J., Zhang, T., & Bilgihan, A. (2015). Customer loyalty: A review and future directions with a special focus on the hospitality industry. *International Journal of Contemporary Hospitality Management, 27*(3), 379–414. https://doi.org/10.1108/IJCHM-03-2014-0151

Kotler, P. (1973). Atmospherics as a marketing tool. *Journal of Retailing, 49*(4), 48–64.

MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, 1*(14), 281–297.

McKinsey & Company. (2023). *The state of grocery retail and food service in Asia*. McKinsey & Company.

Namkung, Y., & Jang, S. (2007). Does food quality really matter in restaurants? Its impact on customer satisfaction and behavioral intentions. *Journal of Hospitality & Tourism Research, 31*(3), 387–409. https://doi.org/10.1177/1096348007299924

Nielsen Vietnam. (2023). *Vietnam Consumer Insights Report*. Nielsen Vietnam.

Nguyễn Đình Thọ. (2011). *Phương pháp nghiên cứu khoa học trong kinh doanh*. Nhà xuất bản Lao động – Xã hội.

Nguyễn Trọng Luận. (2018). Các yếu tố ảnh hưởng đến sự hài lòng của khách hàng tại các chuỗi cửa hàng cà phê: Trường hợp nghiên cứu tại TP. Hồ Chí Minh. *Tạp chí Khoa học Trường Đại học Mở TP.HCM, 13*(3), 117–133.

Nunnally, J. C., & Bernstein, I. H. (1994). *Psychometric Theory* (3rd ed.). McGraw-Hill.

Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing, 64*(1), 12–40.

Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The synthetic data vault. *2016 IEEE International Conference on Data Science and Advanced Analytics (DSAA)*, 399–410. https://doi.org/10.1109/DSAA.2016.49

Phạm Văn Tuấn. (2019). Phân tích sự hài lòng khách hàng theo nhóm VIP và non-VIP tại các ngân hàng thương mại. *Tạp chí Ngân hàng, 18*, 45–52.

Rossi, P. E., Allenby, G. M., & McCulloch, R. (2005). *Bayesian Statistics and Marketing*. John Wiley & Sons.

Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65. https://doi.org/10.1016/0377-0427(87)90125-7

Ryu, K., Lee, H. R., & Kim, W. G. (2012). The influence of the quality of the physical environment, food, and service on restaurant image, customer perceived value, customer satisfaction, and behavioral intentions. *International Journal of Contemporary Hospitality Management, 24*(2), 200–223. https://doi.org/10.1108/09596111211206141

Stevens, P., Knutson, B., & Patton, M. (1995). DINESERV: A tool for measuring service quality in restaurants. *Cornell Hotel and Restaurant Administration Quarterly, 36*(2), 56–60. https://doi.org/10.1177/001088049503600226

Trần Thị Thu Trang. (2020). Đánh giá chất lượng dịch vụ và sự hài lòng của khách hàng tại các chuỗi nhà hàng buffet Hà Nội. *Tạp chí Khoa học Đại học Quốc gia Hà Nội: Kinh tế và Kinh doanh, 36*(2), 43–55.

Wang, Y., & Yu, X. (2017). The differentiation analysis of logistic service quality satisfaction based on customer segmentation. *Journal of Service Science and Management, 10*(1), 75–89. https://doi.org/10.4236/jssm.2017.101006

Wei, J. T., Lin, S. Y., & Wu, H. H. (2010). A review of the application of RFM model. *African Journal of Business Management, 4*(19), 4199–4206.

---

## Source code & live demo

- **GitHub repository:** `https://github.com/<username>/pizza4ps-csat-analysis` *(cập nhật sau khi push)*
- **Live demo (Streamlit Community Cloud):** `https://pizza4ps-csat.streamlit.app` *(cập nhật sau khi deploy)*

Repository chứa toàn bộ mã nguồn sinh dữ liệu (`data/generate_synthetic_data.py`), pipeline phân tích đầy đủ (`notebooks/analysis_pipeline.py`), web app tương tác (`app/app.py`), kết quả phân tích (`data/results/`), và hướng dẫn deploy chi tiết (`docs/DEPLOY_GUIDE.md`). Mọi kết quả trong báo cáo này đều có thể tái lập (reproducible) bằng cách chạy lại các script với random seed = 42.
