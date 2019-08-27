# -*- coding: utf-8 -*-
import scrapy
import re
from test1Spider.items import Test1SpiderItem

class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['bcactc.com']
    start_urls = ['http://www.bcactc.com/home/gcxx/now_sgzbgg.aspx']

    def parse(self, response):
        values = response.xpath('//div[@style="float:right"]/text()[1]').get()
        print(values)
        values = values.split()
        values = values[-1]
        index1 = values.find(':', 1)
        index2 = values.find('/', 1)
        this_page = int(values[index1+4:index2])
        last_page = int(values[index2+1:])

        print(last_page)
        print(this_page)
        detail_list1s = response.xpath('//tr[@class = "gridview1_RowStyle"]/td[1]/text()').extract()
        print(len(detail_list1s))
        for detail_list in detail_list1s:
            next_url = 'http://www.bcactc.com/home/gcxx/sgzbgg_new_show.aspx?ggid='+detail_list+'&publicsource=1'
            print(next_url)
            items = Test1SpiderItem()
            items['ProjectNumber'] = detail_list
            yield scrapy.Request(next_url,callback=self.detail_parse,meta={'item': items})
        detail_list2s = response.xpath('//tr[@class = "gridview1_AlternatingRowStyle"]/td[1]/text()').extract()
        for detail_list in detail_list2s:
            next_url = 'http://www.bcactc.com/home/gcxx/sgzbgg_new_show.aspx?ggid='+detail_list+'&publicsource=1'
            print(next_url)
            items = Test1SpiderItem()
            items['ProjectNumber'] = detail_list
            yield scrapy.Request(next_url,callback=self.detail_parse,meta={'item': items})
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
            yield scrapy.FormRequest(url=response.url, formdata= post_data,callback=self.parse, dont_filter=True)
    def detail_parse(self, response):
        items = response.meta['item']
        xiangmu = response.xpath('//table[@class="hei_text"]//tr[3]/td/u[1]/text()').extract_first()
        didian = response.xpath('//table[@class="hei_text"]//tr[4]/td/u[1]/text()').extract_first()
        mianji = response.xpath('//table[@class="hei_text"]//tr[4]/td/u[2]/text()').extract_first()
        gujia = response.xpath('//table[@class="hei_text"]//tr[4]/td/u[3]/text()').extract_first()
        fanwei = response.xpath('//table[@class="hei_text"]//tr[4]/td/u[6]/text()').extract_first()
        zbr = response.xpath('//table[@class="hei_text"]//tr[2]/td[1]/u[1]/text()').extract_first()
        dizhi = response.xpath('//table[@class="hei_text"]//tr[2]/td[1]/u[2]/text()').extract_first()
        lianxiren = response.xpath('//table[@class="hei_text"]//tr[2]/td[1]/u[4]/text()').extract_first()
        dianhua = response.xpath('//table[@class="hei_text"]//tr[2]/td[1]/u[5]/text()').extract_first()
        dljg = response.xpath('//table[@class="hei_text"]//tr[2]/td[2]/u[1]/text()').extract_first()
        dldz = response.xpath('//table[@class="hei_text"]//tr[2]/td[2]/u[2]/text()').extract_first()
        dllianxiren = response.xpath('//table[@class="hei_text"]//tr[2]/td[2]/u[4]/text()').extract_first()
        dldianhua = response.xpath('//table[@class="hei_text"]//tr[2]/td[2]/u[5]/text()').extract_first()
        jieshushijian = response.xpath('//table[@class="hei_text"]//tr[7]/td[1]/u[2]/text()').extract_first()
        items['ProjectName'] = xiangmu.strip()
        items['ProjectLocation'] = didian.strip()
        items['ProjectSize'] = mianji.strip()
        items['BiddingBudget'] = gujia.strip()
        items['BiddingScope'] = fanwei.strip()
        items['BiddingCompany'] = zbr.strip()
        items['BiddingContact'] = lianxiren.strip()
        items['BiddingAddress'] = dizhi.strip()
        items['BiddingContactTel'] = dianhua.strip()
        items['BiddingAgencyCompany'] = dljg.strip()
        items['BiddingAgencyAddress'] = dldz.strip()
        items['BiddingAgencyContact'] = dllianxiren.strip()
        items['BiddingAgencyContactTel'] = dldianhua.strip()
        items['BiddingEndDate'] = jieshushijian.strip()
        print(items)
        # yield items