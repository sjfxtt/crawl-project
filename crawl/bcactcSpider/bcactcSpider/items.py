# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BcactcspiderItem(scrapy.Item):
    Number = scrapy.Field()
    # 工程编号
    UnitName = scrapy.Field()
    # 单位名称
    ProjectName = scrapy.Field()
    # 工程名称
    Place = scrapy.Field()
    # 建设地点
    WinningBidder = scrapy.Field()
    # 中标人
    WinningBidPrice = scrapy.Field()
    # 中标价(元)
    PublicityStartTime = scrapy.Field()
    # 公示开始时间