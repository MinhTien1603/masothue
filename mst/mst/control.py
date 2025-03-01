import subprocess
import threading
import pandas as pd
import os
import logging

# Cấu hình
INPUT_FILE = "data/masothue_backfill_202501201319_6.csv"
OUTPUT_DIR = "output/"
OUTPUT_FILES = [f"{OUTPUT_DIR}/output_{i+1}.csv" for i in range(6)]
BATCH_SIZE = 1000
NUM_THREADS = 6  # Chỉ sử dụng 6 luồng để không bị ghi đè file

# Tạo thư mục output nếu chưa có
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_remaining_batches():
    """Tải danh sách URL chưa crawl bằng cách đối chiếu với 6 file output."""
    df_input = pd.read_csv(INPUT_FILE, encoding="utf-8")

    # Kiểm tra danh sách đã crawl
    crawled_urls = set()
    for file in OUTPUT_FILES:
        if os.path.exists(file):
            df_output = pd.read_csv(file, encoding="utf-8")
            if "mst_url" in df_output.columns:
                crawled_urls.update(df_output["mst_url"].dropna().astype(str).tolist())

    # Lọc ra các URL chưa crawl
    df_remaining = df_input[~df_input["mst_url"].astype(str).isin(crawled_urls)]
    return [df_remaining[i:i + BATCH_SIZE] for i in range(0, len(df_remaining), BATCH_SIZE)]


def run_scrapy_job(df_batch, thread_id):
    """Chạy Scrapy trên từng batch và lưu kết quả vào 1 trong 6 file cố định."""
    logging.info(f"Thread-{thread_id} đang xử lý {len(df_batch)} URL...")

    urls = list(df_batch["mst_url"])
    urls_frm = str(urls).replace("'", '"')

    # Chạy Scrapy với batch hiện tại
    command = f"""
        cd mst
        scrapy crawl mst
    """
    subprocess.run(command, shell=True, check=True)

    # Chọn 1 trong 6 file để lưu batch này
    output_file = OUTPUT_FILES[thread_id % 6]

    # Kiểm tra file có dữ liệu hay không để ghi header
    write_header = not os.path.exists(output_file) or os.stat(output_file).st_size == 0

    df_batch.to_csv(output_file, mode="a", header=write_header, index=False, encoding="utf-8")

    logging.info(f"Thread-{thread_id} đã lưu kết quả vào {output_file}")


def start_threads():
    """Khởi chạy các batch song song trên nhiều luồng, tiếp tục từ nơi đã dừng."""
    batches = load_remaining_batches()

    threads = []
    for i in range(0, len(batches), NUM_THREADS):
        for j in range(NUM_THREADS):
            if i + j >= len(batches):
                break  # Không còn batch để chạy

            thread = threading.Thread(target=run_scrapy_job, args=(batches[i + j], j))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # Đợi các luồng hoàn thành trước khi chạy batch tiếp theo

    print("Tất cả các batch đã hoàn thành.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_threads()
