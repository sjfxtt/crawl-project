# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1SpiderItem(scrapy.Item):
    ProjectNumber = scrapy.Field()
    ProjectName = scrapy.Field()
    ProjectLocation = scrapy.Field()
    ProjectSize = scrapy.Field()
    BiddingBudget = scrapy.Field()
    BiddingScope = scrapy.Field()
    BiddingCompany = scrapy.Field()
    BiddingContact = scrapy.Field()
    BiddingAddress = scrapy.Field()
    BiddingContactTel = scrapy.Field()
    BiddingAgencyCompany = scrapy.Field()
    BiddingAgencyAddress = scrapy.Field()
    BiddingAgencyContact = scrapy.Field()
    BiddingAgencyContactTel = scrapy.Field()
    BiddingEndDate = scrapy.Field()