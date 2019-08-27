# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ConstinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 按照上面的格式进行修改
    ChildMenu4 = scrapy.Field()
    # 项目分类
    Menu4Link = scrapy.Field()
    # 一级链接
    DetailLink = scrapy.Field()
    # 二级链接
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
    Classify = scrapy.Field()
    #类别



