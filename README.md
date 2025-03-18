# Masothue Scraping Project
 Đây là một dự án thu thập dữ liệu mã số thuế từ danh sách đường dẫn công ty trong một tệp CSV bằng Python.
***
 ## Mô tả
 ### Mục đích: Tự động thu thập mã số thuế từ các trang web của công ty và lưu kết quả vào CSV
 ### Công cụ sử dụng: Scrapy 
 ### Kết quả: Dữ liệu được lưu vào thư mục output/ dưới dạng mst_output.csv
***
 ## Cấu trúc thư mục
 mst/
├── data/
│   └── masothue_backfill_202501201...  # data
├── mst/
│   ├── spiders/                        # Spider files for scraping
│        ├── __init__.py
│        ├──  mst.py
│   ├── __init__.py
│   ├── control.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── output/
│   └── mst_output.csv                  # Output data file
├── .env                                # Environment variables
├── scrapy.cfg                          # Scrapy configuration
├── .gitignore                          # Git ignore file
└── requirements.txt                    # Project dependencies
***
# Yêu cầu
Python 3.1 trở lên
Git (để quản lý mã nguồn)
Kiến thức cơ bản về Python và Scrapy
***
# Cài đặt
## Clone repository

'''git clone https://github.com/MinhTien1603/masothue.git
   cd masothue '''

## Cài đặt thư viện cần thiết

''' python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    pip install -r requirements.txt'''

## Cấu hình biến môi trường
Chỉnh sửa file .env nếu cần:
'''
INPUT_FILE=data/masothue_backfill_202501201319_6.csv  
OUTPUT_DIR=output/
BATCH_SIZE=1000  
NUM_THREADS=6 
'''
