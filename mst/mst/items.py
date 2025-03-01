# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MstItem(scrapy.Item):
    mst_taxid = scrapy.Field()
    mst_company_name = scrapy.Field()
    mst_company_name_in_short = scrapy.Field()
    mst_forg_orgname = scrapy.Field()
    mst_address = scrapy.Field()
    mst_main_business_code = scrapy.Field()
    mst_business_type = scrapy.Field()
    mst_representative = scrapy.Field()
    mst_phone_number = scrapy.Field()
    mst_active_date = scrapy.Field()
    mst_managed_by = scrapy.Field()
    mst_company_type = scrapy.Field()
    mst_status = scrapy.Field()
    mst_last_updated = scrapy.Field()
    mst_url = scrapy.Field()
    mst_timestamp = scrapy.Field()

