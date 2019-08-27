# -*- coding: utf-8 -*-
import scrapy
import re
from zjwSpider.items import ZjwspiderItem
class ZjwSpider(scrapy.Spider):
    name = 'zjw'
    allowed_domains = ['zjw.beijing.gov.cn']
    # start_urls = ['http://zjw.beijing.gov.cn/eportal/ui?pageId=314738']
    start_urls = [f'http://zjw.beijing.gov.cn/eportal/ui?pageId=314738&currentPage={page}' for page in range(1,201)]

    def parse(self, response):
        selectors = response.xpath('//td[@style="text-align: center;"]/a/@href').extract()
        print(selectors)
        for select in selectors:
            next_url = 'http://zjw.beijing.gov.cn'+select
            print(next_url)
            yield scrapy.Request(next_url,callback=self.detail_parse)
    def detail_parse(self,response):
        item = ZjwspiderItem()
        item['ProjectName'] = response.xpath('//table[@class="detailview"]//tr[1]/td[2]/text()').extract()[0].strip()
        item['ProjectNumber'] = response.xpath('//table[@class="detailview"]//tr[2]/td[2]/text()').extract()[0].strip()
        item['VendorName'] = response.xpath('//table[@class="detailview"]//tr[3]/td[2]/text()').extract()[0].strip()
        item['VendorContact'] = response.xpath('//table[@class="detailview"]//tr[4]/td[2]/text()').extract()[0].strip()
        item['VendorPM'] = response.xpath('//table[@class="detailview"]//tr[5]/td[2]/text()').extract()[0].strip()
        item['ContractType'] = response.xpath('//table[@class="detailview"]//tr[6]/td[2]/text()').extract()[0].strip()
        item['ContractSize'] = response.xpath('//table[@class="detailview"]//tr[7]/td[2]/text()').extract()[0].strip()
        item['ContractCounty'] = response.xpath('//table[@class="detailview"]//tr[8]/td[2]/text()').extract()[0].strip()
        item['ContractorName'] = response.xpath('//table[@class="detailview"]//tr[3]/td[4]/text()').extract()[0].strip()
        item['ContractorContact'] = response.xpath('//table[@class="detailview"]//tr[4]/td[4]/text()').extract()[0].strip()
        item['ContractorPM'] = response.xpath('//table[@class="detailview"]//tr[5]/td[4]/text()').extract()[0].strip()
        item['ContractDate'] = response.xpath('//table[@class="detailview"]//tr[6]/td[4]/text()').extract()[0].strip()
        item['ContractAmount'] = response.xpath('//table[@class="detailview"]//tr[7]/td[4]/text()').extract()[0].strip()
        item['ContractAddress'] = response.xpath('//table[@class="detailview"]//tr[8]/td[4]/text()').extract()[0].strip()
        yield item