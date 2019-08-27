# -*- coding: utf-8 -*-
import scrapy

class Bcact1Spider(scrapy.Spider):
    name = 'bcact1'
    allowed_domains = ['bcactc.com']
    start_urls = ['http://www.bcactc.com/home/gcxx/index.aspx?gs=&sg_gs=']

    def parse(self, response):
        # urls = response.xpath('//ul[@id = "ChildMenu3"]/li/a/@href').extract()
        # print(urls)
        # for url in urls:
        url = 'http://www.bcactc.com/home/gcxx/' + 'now_kcsjzbgs.aspx'
        yield scrapy.Request(url, callback=self.detail_parse, dont_filter=True)
    def detail_parse(self, response):
        values = response.xpath('//*[@id="Form1"]/div[2]/div/text()').extract_first()
        values = values.split()
        print(values)
        v = values[-1].split()
        last_page = int(v[0][-1])
        this_page = int(v[0][-3])
        print(last_page)
    #
        detail_list1s = response.xpath('//tr[@class = "gridview1_RowStyle"]//td/a/@href').extract()
        print(detail_list1s)
        # detail_list2s = response.xpath('//tr[@class = "gridview1_AlternatingRowStyle"]//td/a/@href').extract()
        # for detail_list in detail_list1s:
        #     next_url = 'http://www.bcactc.com/home/gcxx/' + detail_list
        #     yield scrapy.Request(next_url, callback=self.inner_parse)
        # for detail_list in detail_list2s:
        #     next_url = 'http://www.bcactc.com/home/gcxx/'+detail_list
        #     yield scrapy.Request(next_url,callback=self.inner_parse)
        if this_page < last_page:
            a = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first()
            b = response.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
            c = response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
            post_data = {
                "__EVENTTARGET": "PagerControl1$_ctl4",
                "__EVENTARGUMENT": "",
                "__LASTFOCUS": "",
                "__VIEWSTATE": a,
                "__VIEWSTATEGENERATOR": b,
                "__EVENTVALIDATION": c,
                "gcbh_Text_Box": "",
                "gcmc_TextBox": "",
                "PagerControl1:_ctl4": "{}".format(this_page+1),
            }
            yield scrapy.FormRequest(url=response.url, formdata= post_data,callback=self.detail_parse, dont_filter=True)
    # def inner_parse(self, response):
    #     name = response.xpath('//*[@id="gcmc"]/text()').extract_first().split()[0]
    #     item = {
    #         'name':name
    #     }
    #     yield item