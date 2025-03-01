# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MstPipeline:
    def open_spider(self, spider):
        self.file = open("output/mst_output.csv", "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            "mst_taxid", "mst_company_name", "mst_company_name_in_short", "mst_forg_orgname",
            "mst_address", "mst_main_business_code", "mst_business_type", "mst_representative",
            "mst_phone_number", "mst_active_date", "mst_managed_by", "mst_company_type",
            "mst_status", "mst_last_updated", "mst_url", "mst_timestamp"
        ])

    def process_item(self, item, spider):
        self.writer.writerow([
            item.get("mst_taxid", ""),
            item.get("mst_company_name", ""),
            item.get("mst_company_name_in_short", ""),
            item.get("mst_forg_orgname", ""),
            item.get("mst_address", ""),
            item.get("mst_main_business_code", ""),
            item.get("mst_business_type", ""),
            item.get("mst_representative", ""),
            item.get("mst_phone_number", ""),
            item.get("mst_active_date", ""),
            item.get("mst_managed_by", ""),
            item.get("mst_company_type", ""),
            item.get("mst_status", ""),
            item.get("mst_last_updated", ""),
            item.get("mst_url", ""),
            item.get("mst_timestamp", ""),
        ])
        return item

    def close_spider(self, spider):
        self.file.close()
