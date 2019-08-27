# -*- coding: utf-8 -*-
import scrapy #爬虫文件

#爬虫类，继承自Spider
class GocilidbSpider(scrapy.Spider):
    name = 'gocilidb'#爬虫文件
    allowed_domains = ['gocilidb.com']#只能在这个域名下采集
    start_urls = ['http://gocilidb.com/page/%E6%95%B0%E5%AD%A6/1-0-0.shtml']#开始采集的网站

    def parse(self, response):#提取数据，提取新的网址，response是响应内容，下载器下载的
        #查看第一页网址
        print(response.url)
        #1.翻页的实现
        next_pages = response.xpath('//div[@class="pages"]/a/@href').extract()#提取出来
        if next_pages:
            for url in next_pages:
                next_url = 'http://gocili.com'+url
                #对下一页发送请求 yield是生成器
                yield scrapy.Request(next_url,callback=self.parse)
        #2.提取详情页信息
        detail_urls = response.xpath('//div[@class="list_area"]/dl/dt/a/@href').extract()
        if detail_urls:
            for u in detail_urls:
                # 拼接完整的网址 第二种方法
                detail_url=response.urljoin(u)
                #发送详情页的请求
                yield scrapy.Request(detail_url,callback=self.parse_detail)
    def parse_detail(self,response):
        #3.提取数据
        magnet_url = response.xpath('//p[@class="dd magnet"]/a/@href').extract_first()
        if magnet_url:
            print(magnet_url)#打印提取的数据
        #4.提取全部喜欢的信息
        like_urls = response.xpath('//div[@calss="dd rtorrents"]/p/a/@href').extract()
        if like_urls:
            for like_url in like_urls:
                like_url = response.urljoin(like_url)
                #再次发送请求
                yield scrapy.Request(like_url, callback=self.parse_detail)




