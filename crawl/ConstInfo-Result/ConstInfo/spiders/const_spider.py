# -*- coding: utf-8 -*-
import scrapy
from ConstInfo.items import ConstinfoItem


# 继承类
class ConstSpiderSpider (scrapy.Spider):
    name = 'const_spider'
    allowed_domains = ['www.bcactc.com']  # 入口URL，扔到调度器里面去
    start_urls = ['http://www.bcactc.com/home/gcxx/index.aspx?zbjg&sg_zbjg']

    # 之后engine把这些扔到downloader下载解析
    # 在parse中进行解析
    # 一级页面的爬取
    def parse(self, response):
#        project_list = response.xpath('//ul[@id="ChildMenu4"]/li')
#        # 先抓取一大块
#        # 之后再对细节进行爬取
#        for c_item in project_list:  # item文件导进来
#            const_item = ConstinfoItem()  # 写详细的xpath，进行数据的解析
#            const_item['ChildMenu4'] = c_item.xpath('.//a/text()').extract_first()
#            # print(const_item['ChildMenu4'])
#            const_item['Menu4Link'] = c_item.xpath('.//a/@href').extract_first()
#            # 把数据放到item pipline 当中
#            # yield const_item
#            yield scrapy.Request("http://www.bcactc.com/home/gcxx/"+const_item['Menu4Link'],
#                                 meta={'const_item': const_item}, callback=self.detail_parse)
#            # meta把变量传到下一个函数
#            # yield const_item['ChildMenu4']
            # 根据内页地址爬取
            # 每次解析一个项目的表单
        from sqlalchemy import create_engine
        import pandas as pd
        engine = create_engine('mssql+pymssql://it.intern:lsh#123@sql04.lshmnc.com.cn:1433/PYTHON_LAB')
        pdf = pd.read_sql("select ID,TypeName from [dbo].[SalesLeads_MainType]",engine)
        for pi in range(len(pdf)):
            pa = pdf.iloc[pi,0]
            df = pd.read_sql("select TypeName,SourceUrl from SalesLeads_SubType where ParentID={}".format(pa),engine)

            for i in range(len(df)):
                a = df.iloc[i,0]
                b = df.iloc[i,1]
                const_item = ConstinfoItem()  # 写详细的xpath，进行数据的解析
                const_item['ChildMenu4'] = a
                # print(const_item['ChildMenu4'])
                const_item['Menu4Link'] = b
                # 把数据放到item pipline 当中
                # yield const_item
                yield scrapy.Request("http://www.bcactc.com/home/gcxx/"+b+'&random=1234',meta={'const_item': const_item}, callback=self.detail_parse)
                             
                               


    def detail_parse(self, response):
        values = response.xpath('//*[@id="Form1"]/div[2]/div/text()').extract_first()
        if values is not None:
            print(values)
            print('*************')
            values = values.split()
            v = values[-1].split()
            last_page = int(v[0][-1])
            this_page = int(v[0][-3])#获取页码
            # print(response.text)
            const_item = response.meta['const_item']

            # 因为单双数的class不一样，要用两个变量储存
            detail1 = response.xpath('//table[@id="MyGridView1"]/tr[@class="gridview1_RowStyle"]')
            detail2 = response.xpath('//table[@id="MyGridView1"]/tr[@class="gridview1_AlternatingRowStyle"]')
            for detail_link1 in detail1:
                const_item['DetailLink'] = detail_link1.xpath('.//td[@class="gridview_RowTD"]/a/@href').extract_first()
                yield scrapy.Request("http://www.bcactc.com/home/gcxx/"+const_item['DetailLink'],
                                     meta={'const_item': const_item}, callback=self.inner_parse)

            for detail_link2 in detail2:
                const_item['DetailLink'] = detail_link2.xpath('.//td[@class="gridview_RowTD"]/a/@href').extract_first()
                yield scrapy.Request("http://www.bcactc.com/home/gcxx/" + const_item['DetailLink'],
                                     meta={'const_item': const_item}, callback=self.inner_parse)
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
                yield scrapy.FormRequest(url=response.url, formdata= post_data, callback=self.detail_parse, meta={'const_item': const_item}, dont_filter=True)
    def inner_parse(self, response):
        const_item = response.meta['const_item']
        innerInfo = response.xpath('//table[@class="hei_text"]')
        const_item['Number'] = "".join(innerInfo.xpath('normalize-space(.//tr[2]/td[2]/text())').extract_first().split())
        const_item['UnitName'] = "".join(innerInfo.xpath('normalize-space(.//tr[3]/td[2]/text())').extract_first().split())
        const_item['ProjectName'] = "".join(innerInfo.xpath('normalize-space(.//tr[4]/td[2]/text())').extract_first().split())
        const_item['Place'] = "".join(innerInfo.xpath('normalize-space(.//tr[5]/td[2]/text())').extract_first().split())
        const_item['WinningBidder'] = "".join(innerInfo.xpath('normalize-space(.//tr[6]/td[2]/text())').extract_first().split())
        const_item['WinningBidPrice'] = "".join(innerInfo.xpath('normalize-space(.//tr[7]/td[2]/text())').extract_first().split())
        const_item['PublicityStartTime'] = "".join(innerInfo.xpath('normalize-space(.//tr[8]/td[2]/text())').extract_first().split())
        # yield const_item
        print(const_item)
        print('*********************')












