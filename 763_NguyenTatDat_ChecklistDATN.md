## 

## Mục tiêu chính của đề cương

* Xây dựng hệ thống phân tích giỏ hàng sử dụng thuật toán Apriori.  
* Tìm các luật kết hợp có ý nghĩa từ dữ liệu giao dịch.  
* Xây dựng module gợi ý sản phẩm dựa trên luật kết hợp.  
* Đánh giá hiệu quả bằng các chỉ số support, confidence, lift.  
* Thiết kế hệ thống gồm:  
  * frontend (giao diện người dùng),  
  * backend (xử lý Apriori),  
  * database (lưu trữ dữ liệu).  
* Cho phép:  
  * upload dữ liệu CSV,  
  * tiền xử lý dữ liệu,  
  * chạy thuật toán Apriori,  
  * hiển thị tập phổ biến, luật kết hợp và gợi ý sản phẩm.  
* Kết luận và chứng minh Apriori có thể ứng dụng hiệu quả trong gợi ý mua hàng

## Hiện tại bạn đã làm được

* Xây dựng giao diện đăng nhập / đăng ký bằng customtkinter.  
* Lưu tài khoản người dùng vào SQLite và mã hóa mật khẩu bằng SHA-256.  
* Phân quyền cơ bản: admin mới có nút Upload CSV và Quản lý User.  
* Hiển thị danh sách user trong cửa sổ User Manager.  
* Cho phép upload file CSV và hiển thị nội dung file dưới dạng bảng trong GUI.

## Những phần còn thiếu so với đề tài

### 1\. Thuật toán Apriori

* Chưa có cài đặt Apriori (mlxtend hoặc apyori).  
* Chưa có xử lý tạo frequent itemsets và luật kết hợp.

### 2\. Tiền xử lý dữ liệu giỏ hàng

* Chưa có bước xử lý dữ liệu từ CSV sang danh sách giao dịch.  
* Chưa xử lý dữ liệu thiếu, dữ liệu nhãn, chuẩn hóa sản phẩm.

### 3\. Gợi ý sản phẩm

* Chưa có module gợi ý sản phẩm dựa trên luật kết hợp.  
* Chưa hiển thị đề xuất sản phẩm cho khách hàng.

### 4\. Đánh giá kết quả

* Chưa tính toán support, confidence, lift.  
* Chưa hiển thị hoặc lọc các luật có ý nghĩa.

### 5\. Thiết kế hệ thống / cơ sở dữ liệu

* Chỉ có bảng users; thiếu bảng Product, Transaction, TransactionDetail.  
* Chưa lưu trữ kết quả phân tích hoặc luật vào database.

## Kết luận

Bạn đã hoàn thành phần:

* xác thực người dùng,  
* cho phép admin upload CSV,  
* hiển thị dữ liệu CSV.

Nhưng bạn còn thiếu phần cốt lõi của đề tài:

* Apriori \+ khai phá luật,  
* gợi ý sản phẩm,  
* đánh giá luật,  
* thiết kế dữ liệu giao dịch và lưu trữ kết quả.

