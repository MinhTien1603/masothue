# Masothue Scraping Project
 Đây là một dự án thu thập dữ liệu mã số thuế từ danh sách đường dẫn công ty trong một tệp CSV bằng Python.
***
 ## Mô tả
 Mục đích: Tự động thu thập mã số thuế từ các trang web của công ty và lưu kết quả vào CSV  
 Công cụ sử dụng: Scrapy  
 Kết quả: Dữ liệu được lưu vào thư mục output/ dưới dạng mst_output.csv  
***
# Yêu cầu
Python 3.1 trở lên  
Git (để quản lý mã nguồn)  
Kiến thức cơ bản về Python và Scrapy  
***
# Cài đặt
## Clone repository
    git clone https://github.com/MinhTien1603/masothue.git
    cd masothue 

## Cài đặt thư viện cần thiết
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    pip install -r requirements.txt

# Cách sử dụng
## Chạy spider
    scrapy crawl mst
## Kiểm tra kết quả
Sau khi chạy xong, mở output/mst_output.csv để xem dữ liệu đã thu thập.
## Tuỳ chỉnh cài đặt
Chỉnh sửa mst/settings.py để thay đổi tốc độ crawl, user-agent, delay, v.v.  
Chỉnh sửa .env để thay đổi đường dẫn tệp đầu vào (INPUT_FILE), thư mục đầu ra (OUTPUT_DIR), kích thước lô xử lý (BATCH_SIZE), và số luồng (NUM_THREADS).  

# Liên hệ
Nếu có thắc mắc, vui lòng mở issue trên GitHub repository hoặc liên hệ qua email 23521579@gm.uit.edu.vn
