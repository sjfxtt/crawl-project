# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['bcactc.com']
    start_urls = ['http://www.bcactc.com/home/gcxx/now_zbjggs.aspx?type=sg']

    def parse(self, response):
        values = response.xpath('//*[@id="Form1"]/div[2]/div/text()').extract_first()
        print(values)
        values = values.split()
        v = values[-1].split()
        last_page = int(v[0][-1])
        this_page = int(v[0][-3])#获取页码
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
            yield scrapy.FormRequest(url=response.url, formdata= post_data, callback=self.parse, dont_filter=True)
