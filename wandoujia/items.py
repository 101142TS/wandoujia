# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WandoujiaMainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    data_app_id = scrapy.Field()        #编号     
    data_app_name = scrapy.Field()      #名称

    data_app_pname = scrapy.Field()     #包名
    data_app_vname = scrapy.Field()     #版本代号
    
    download_url = scrapy.Field()       #下载链接
    size = scrapy.Field()               #大小
    update_time = scrapy.Field()        #更新时间
    download_cnt = scrapy.Field()       #下载量
