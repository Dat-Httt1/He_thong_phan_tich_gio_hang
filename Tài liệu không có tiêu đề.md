 

|  |   TRƯỜNG ĐẠI HỌC THUỶ LỢI KHOA CÔNG NGHỆ THÔNG TIN     BẢN TÓM TẮT ĐỀ CƯƠNG ĐỒ ÁN TỐT NGHIỆP   |
| :---- | ----- |

**Tên đề tài: Ứng dụng thuật toán Apriori để xây dựng hệ thống phân tích giỏ hàng**

*Sinh viên thực hiện*: Nguyễn Tất Đạt

*Lớp*:   63HTTT1

*Mã sinh viên:* 2151160524

*Số điện thoại: 0327222834*

*Email:* 2151160524@e.tlu.edu.vn

*Giáo viên hướng dẫn*: TS.Đỗ Oanh Cường    	          Email: cuongdo@e.tlu.edu.vn

                           	  

                           	 

**TÓM TẮT ĐỀ TÀI**

Khi khách hàng mua sắm trực tuyến, họ thường lựa chọn nhiều sản phẩm khác nhau trong cùng một giao dịch. Nếu có thể phát hiện được những nhóm sản phẩm thường xuyên được mua cùng nhau, doanh nghiệp có thể tận dụng thông tin này để đề xuất sản phẩm phù hợp, triển khai chương trình khuyến mãi chéo, hoặc sắp xếp hàng hóa hiệu quả hơn. Đây chính là bài toán khai phá luật kết hợp – một hướng nghiên cứu thực tiễn trong lĩnh vực học máy, mang lại giá trị thiết thực cho hoạt động kinh doanh hiện nay

Trong bối cảnh thương mại điện tử và bán lẻ phát triển mạnh mẽ, việc hiểu rõ hành vi mua sắm của khách hàng trở nên vô cùng quan trọng. Đề tài này tập trung vào việc ứng dụng thuật toán Apriori – một phương pháp khai phá luật kết hợp phổ biến – nhằm phân tích dữ liệu giỏ hàng và phát hiện mối quan hệ giữa các sản phẩm thường được mua cùng nhau.

Kết quả của quá trình khai phá được sử dụng để xây dựng module gợi ý sản phẩm, giúp doanh nghiệp đưa ra chiến lược bán hàng hiệu quả, tăng doanh thu và nâng cao trải nghiệm khách hàng.

module được cài đặt bằng ngôn ngữ lập trình Python, sử dụng thư viện mlxtend hoặc apyori để triển khai thuật toán, và dữ liệu được xử lý, trực quan hóa bằng pandas, matplotlib.

**CÁC MỤC TIÊU CHÍNH**

 

\-        Tìm các luật kết hợp có ý nghĩa từ dữ liệu giỏ hàng.

\-        Xây dựng module gợi ý sản phẩm dựa trên luật kết hợp.

\-        Đánh giá hiệu quả thông qua các chỉ số support, confidence, lift.

 

**NỘI DUNG CHÍNH**

●      Tổng quan lý thuyết:

○      Trình bày khái niệm về khai phá dữ liệu (Data Mining) và luật kết hợp (Association Rule).

○      Giới thiệu thuật toán Apriori, nguyên lý hoạt động, công thức tính support, confidence, lift.

●      Phân tích và xử lý dữ liệu:

○      Thu thập và làm sạch dữ liệu mua hàng (giỏ hàng khách hàng).

○      Chuyển dữ liệu về dạng phù hợp để đưa vào thuật toán Apriori.

●      Trình bày tổng quan về thuật toán Apriori, nguồn gốc và vai trò trong khai phá luật kết hợp (Association Rule Mining).  
●      Giải thích nguyên lý Apriori (Apriori Property).  
●      Mô tả quy trình hoạt động của thuật toán.  
●      Cài đặt và thực nghiệm thuật toán Apriori.  
●      Xây dựng module gợi ý sản phẩm:

○      Ứng dụng các luật kết hợp thu được để gợi ý sản phẩm cho khách hàng.

○      Hiển thị kết quả dưới dạng bảng hoặc giao diện đơn giản.

●      Đánh giá và kết luận:

○      Phân tích ý nghĩa của các luật thu được.

○      Đánh giá hiệu quả module (về tính hợp lý, độ chính xác)

 

**DỮ LIỆU**

 

Ø  **Input đầu vào bài toán**: là một tập các giao dịch đã thanh toán thành công trước đó từ các người mua trước, các hóa đơn, ...

Ø  **Output của bài toán**: là một tập luật kết hợp có độ tin cậy, biểu thị xem xu hướng mua của người mua với các sản phẩm sẵn có ( Sản phẩm A thì sẽ mua thêm sản phẩm B \- If A then B )

 

è Dữ liệu bài toán là 1 file CSV dạng hoá đơn bán hàng

**XÂY DỰNG HỆ THỐNG**

**1\.**	**Kiến trúc hệ thống**

Hệ thống gồm 3 thành phần chính:

* **Frontend:** giao diện người dùng  
* **Backend:** xử lý thuật toán Apriori  
* **Database:** lưu trữ dữ liệu

---

**2\.**	**Các chức năng chính**

·       Upload dữ liệu giao dịch

·       Tiền xử lý dữ liệu

·       Chạy thuật toán Apriori

·       Hiển thị:

o   Tập phổ biến

o   Luật kết hợp

·       Gợi ý sản phẩm

---

**3\.**	**Use Case (nghiệp vụ)**

·       Người dùng:

o   Tải dữ liệu

o   Chạy phân tích

o   Xem kết quả

---

**4\.**	**Thiết kế cơ sở dữ liệu**

Các bảng chính:

·       **Product** (id, name, price)

·       **Transaction** (id, date)

·       **TransactionDetail** (transaction\_id, product\_id)

---

**5\.**	**Luồng xử lý hệ thống**

1\.	Nhập dữ liệu

2\.	Tiền xử lý

3\.	Chạy Apriori

4\.	Sinh luật

5\.	Lưu kết quả

6\.	Hiển thị & gợi ý

 

**KẾT QUẢ DỰ KIẾN**

1. Tập luật kết hợp phản ánh mối quan hệ giữa các sản phẩm.

2. Giao diện hoặc bảng gợi ý sản phẩm cho khách hàng.

3. Minh chứng rằng Apriori có thể ứng dụng hiệu quả trong bài toán gợi ý mua hàng.

 

 

**KẾ HOẠCH THỰC HIỆN**

 

| STT | Thời gian | Nội dung công việc | Kết quả dự kiến đạt được |
| :---: | :---: | :---: | :---: |
| 1 |   Tuần 1 |  Tìm hiểu tổng quan về khai phá dữ liệu và thuật toán Apriori.- Thu thập tài liệu tham khảo (báo cáo, paper, code mẫu)   | Hiểu rõ nguyên lý Apriori và ứng dụng luật kết hợp.   |
| 2 |   Tuần 2-3 | Tìm hiểu về các thuật toán, kỹ thuật tối ưu hóa tham số, mô hình và các kịch bản có thể kết hợp được | Hiểu được một số thuật toán tối ưu, đưa ra được kịch bản kết hợp các mô hình học sâu với thuật toán tối ưu và tổng hợp lại để đưa ra đánh giá về sự phù hợp của các mô hình. |
| 3 |   Tuần 4-5 | Tự thu thập và chuẩn bị dữ liệu | Tập dữ liệu sạch, sẵn sàng cho mô hình   |
| 4 |   Tuần 6-7-8 | Cài đặt thuật toán Apriori bằng Python (dùng thư viện mlxtend hoặc apyori).- Chạy thử với tập dữ liệu nhỏ để kiểm tra kết quả. Sinh luật kết hợp và tính các chỉ số support, confidence, lift. Lọc ra các luật có ý nghĩa cao.Xây dựng phần gợi ý sản phẩm dựa trên luật kết hợp. Thiết kế giao diện đơn giản (CLI, web hoặc Excel dashboard)       | Tìm được các tập phổ biến (frequent itemsets).Danh sách các luật kết hợp mạnh.Mô hình gợi ý hoạt động hoàn chỉnh.       |
| 5 |   Tuần 9-10 | Kiểm tra & hoàn thiện báo cáo | Hoàn thành báo cáo hoàn chỉnh |

 

 

 

 

**TÀI LIỆU THAM KHẢO**

1\. Tài liệu về Python: [https://www.python.org/doc/](https://www.python.org/doc/) 

2\. Tài liệu về thuật toán Apriori trong khai phá dữ liệu: https://viblo.asia/newest

 

   
