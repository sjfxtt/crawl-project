# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor#导入链接提取器
from scrapy.spiders import CrawlSpider, Rule#导入全站爬出和采集规则


class Ygdy8Spider(CrawlSpider):
    name = 'ygdy8'#爬虫名字
    allowed_domains = ['ygdy8.net']#爬虫只在该域名下采集数据
    start_urls = ['https://www.ygdy8.net/index.html']#开始采集的网址
    #采集规则的集合
    rules = (
        #采集导航页电影的部分
        #选择所有带有index的网址
        Rule(LinkExtractor(allow=r'index.html', deny='game')),
        #follow=True意思是是否继续提取
        Rule(LinkExtractor(allow=r'list_\d+_\d+.html', deny='game'), follow=True),#正则表达式\d+代表所有数字
        #提取详情页
        Rule(LinkExtractor(allow=r'/\d+/\d+.html', deny='game'), follow=True,callback='parse_item'),  # 正则表达式\d+代表所有数字
    )

    #解析采集回的数据
    def parse_item(self, response):
        # print(response.url)
        movie = {}
        #提取数据
        #.*?提取换行以外的所有信息
        ftp_url = re.findall('<a href="(.*?)">ftp', response.text)
        ftp_name = re.findall('<title>(.*?)</title>',response.text)
        # print(ftp_name)
        # print(ftp_url)
        print('**************')
        items = {
            'name': ftp_name,
            'link': ftp_url
        }
        yield items
