# -*- coding: utf-8 -*-
import scrapy # 导入scrapy

# 创建爬虫类，并继承自scrapy.Spider-->最基础的类 另外几个类都是继承自这个类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili' # 爬虫名字-->必须唯一
    allowed_domains = ['xicidaili.com'] # 允许采集的域名
    # start_urls = ['https://www.xicidaili.com/nn/5'] # 开始采集的网站
    start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1, 50)]#产生批量网址

    # 解析响应数据，提取数据，或者网站等 response就是网页源码
    def parse(self, response):
        #提取数据

        #提取IP PORT
        selectors = response.xpath('//tr') # 选择所有的tr标签
        #循环遍历tr标签下的td标签
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get() # 在当前节点下继续选择
            port = selector.xpath('./td[3]/text()').get()  # 在当前节点下继续选择

            print(ip, port)
            items = {
                'ip': ip,
                'port': port
            }
            yield items
            # print(ip,port)
        #翻页操作
        # next_page = response.xpath('//a[@class="next_page"]/@href').get()
        # if next_page:
        #     print(next_page)
        #     #拼接网址
        #     next_url = response.urljoin(next_page)
        #     #发出请求Request，callback是回调函数，就是将请求得到的函数交给自己处理
        #     yield scrapy.Request(next_url, callback=self.parse)# 生成器