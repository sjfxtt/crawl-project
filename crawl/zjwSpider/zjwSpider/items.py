# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZjwspiderItem(scrapy.Item):
    ProjectName = scrapy.Field()
    ProjectNumber = scrapy.Field()
    VendorName = scrapy.Field()
    VendorContact = scrapy.Field()
    VendorPM = scrapy.Field()
    ContractorName = scrapy.Field()
    ContractorContact = scrapy.Field()
    ContractorPM = scrapy.Field()
    ContractType = scrapy.Field()
    ContractDate = scrapy.Field()
    ContractSize = scrapy.Field()
    ContractAmount = scrapy.Field()
    ContractCounty = scrapy.Field()
    ContractAddress = scrapy.Field()
    TypeID = scrapy.Field()
    IsEnabled = scrapy.Field()

