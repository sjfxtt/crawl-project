# -*- coding: utf-8 -*-
import scrapy
from bcactcSpider.items import BcactcspiderItem

class BcactcSpider(scrapy.Spider):
    name = 'bcactc'
    allowed_domains = ['bcactc.com']
    start_urls = ['http://www.bcactc.com/home/gcxx/index.aspx?zbjg&sg_zbjg']

    def parse(self, response):
        project_list = response.xpath('//ul[@id="ChildMenu4"]/li')
        # 先抓取一大块
        # 之后再对细节进行爬取
        for c_item in project_list:  # item文件导进来
            a = c_item.xpath('.//a/text()').extract_first()
            b = a.xpath('.//a/@href').extract_first()
            # 把数据放到item pipline 当中
            # yield const_item
            yield scrapy.Request("http://www.bcactc.com/home/gcxx/" + b, callback=self.detail_parse)

    def detail_parse(self, response):
        # print(response.text)
        #     values = response.xpath('//*[@id="Form1"]/div[2]/div/text()').extract_first()

        values = response.xpath('//div[@style="float:right"]/text()[1]').extract_first()
        print(values)
        values = values.split()
        v = values[-1].split()
        last_page = int(v[0][-1])
        this_page = int(v[0][-3])  # 获取页码
        print(this_page)

        # 因为单双数的class不一样，要用两个变量储存
        detail1 = response.xpath('//table[@id="MyGridView1"]/tr[@class="gridview1_RowStyle"]')
        detail2 = response.xpath('//table[@id="MyGridView1"]/tr[@class="gridview1_AlternatingRowStyle"]')
        for detail_link1 in detail1:
            temp= detail_link1.xpath('.//td[@class="gridview_RowTD"]/a/@href').extract_first()
            yield scrapy.Request("http://www.bcactc.com/home/gcxx/" + temp, callback=self.inner_parse)

        for detail_link2 in detail2:
            temp= detail_link2.xpath('.//td[@class="gridview_RowTD"]/a/@href').extract_first()
            yield scrapy.Request("http://www.bcactc.com/home/gcxx/" + temp, callback=self.inner_parse)
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
                "PagerControl1:_ctl4": "{}".format(this_page + 1),
            }
            yield scrapy.FormRequest(url=response.url, formdata=post_data, callback=self.detail_parse, dont_filter=True)

    def inner_parse(self, response):
        innerInfo = response.xpath('//table[@class="hei_text"]')
        const_item = {}
        const_item['Number'] = "".join(innerInfo.xpath('normalize-space(.//tr[2]/td[2]/text())').extract_first().split())
        const_item['UnitName'] = "".join(innerInfo.xpath('normalize-space(.//tr[3]/td[2]/text())').extract_first().split())
        const_item['ProjectName'] = "".join(innerInfo.xpath('normalize-space(.//tr[4]/td[2]/text())').extract_first().split())
        const_item['Place'] = "".join(innerInfo.xpath('normalize-space(.//tr[5]/td[2]/text())').extract_first().split())
        const_item['WinningBidder'] = "".join(innerInfo.xpath('normalize-space(.//tr[6]/td[2]/text())').extract_first().split())
        const_item['WinningBidPrice'] = "".join(innerInfo.xpath('normalize-space(.//tr[7]/td[2]/text())').extract_first().split())
        const_item['PublicityStartTime'] = "".join(innerInfo.xpath('normalize-space(.//tr[8]/td[2]/text())').extract_first().split())
        print(const_item)