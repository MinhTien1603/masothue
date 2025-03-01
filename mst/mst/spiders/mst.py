import scrapy
import pandas as pd
from datetime import datetime
from mst.items import MstItem

class MstSpider(scrapy.Spider):
    name = "mst"

    def start_requests(self):
        try:
            df = pd.read_csv("data/masothue_backfill_202501201319_6.csv")  # Đọc danh sách URL từ CSV
            for _, row in df.iterrows():
                url = row["mst_url"]
                if isinstance(url, str) and url.startswith(('http://', 'https://')):
                    yield scrapy.Request(url=url.strip(), callback=self.parse, meta={"mst_taxid": row["mst_taxid"]})
                else:
                    self.logger.error(f"Lỗi định dạng URL: {url}")
        except Exception as e:
            self.logger.error(f"Lỗi đọc file CSV: {e}")

    def parse(self, response):
        item = MstItem()

        item["mst_taxid"] = response.meta["mst_taxid"]
        item["mst_company_name"] = response.css('th[itemprop="name"] span::text').get(default="").strip()
        item["mst_company_name_in_short"] = response.xpath('//tr[td[contains(text(), "Tên viết tắt")]]/td/span/text()').get(default="").strip()
        item["mst_forg_orgname"] = response.xpath('//tr[td[contains(text(), "Tên quốc tế")]]/td/span/text()').get(default="").strip()
        item["mst_address"] = response.css('td[itemprop="address"] span::text').get(default="").strip()
        item["mst_representative"] = response.xpath('//tr[td[contains(text(), "Người đại diện")]]/td/span/a/text()').get(default="").strip()
        item["mst_phone_number"] = response.css('td[itemprop="telephone"] span::text').get(default="").strip()
        item["mst_active_date"] = response.xpath('//tr[td[contains(text(), "Ngày hoạt động")]]/td/span/text()').get(default="").strip()
        item["mst_managed_by"] = response.xpath('//tr[td[contains(text(), "Quản lý bởi")]]/td/span/text()').get(default="").strip()
        item["mst_company_type"] = response.xpath('//tr[td[contains(text(), "Loại hình DN")]]/td/a/text()').get(default="").strip()
        item["mst_status"] = response.xpath('//tr[td[contains(text(), "Tình trạng")]]/td/a/text()').get(default="").strip()
        item["mst_last_updated"] = response.xpath('//tr[td[contains(text(), "Cập nhật mã số thuế")]]//em/text()').get(default="").strip()
        item["mst_url"] = response.url
        item["mst_timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Lấy danh sách ngành nghề kinh doanh
        all_business_code = []
        mst_main_business_code = ""

        for sector in response.css("table.table tbody tr"):
            sector_id = sector.css("td:nth-child(1) a::text").get(default="").strip()
            is_main = bool(sector.css("td:nth-child(2) strong"))

            if is_main:
                mst_main_business_code = sector_id  # Ghi nhận mã ngành chính

            if sector_id and sector_id != mst_main_business_code:
                all_business_code.append(sector_id)  # Chỉ thêm mã ngành phụ không trùng ngành chính

        # Lưu vào item
        item["mst_main_business_code"] = mst_main_business_code  # Mã ngành chính
        item["mst_business_type"] = ", ".join(all_business_code)  # Danh sách mã ngành phụ (không trùng ngành chính)

        yield item
