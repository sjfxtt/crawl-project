# -*- coding: utf-8 -*-
import scrapy
import re
from doubanSpider.items import DoubanspiderItem
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # start_urls = [f'https://movie.douban.com/top250?start={page*25}&filter=' for page in range(0, 10)]
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    def parse(self, response):
        selectors = response.xpath("//*[@id='content']/div/div[1]/ol/li")
        const_item = DoubanspiderItem()
        for selector in selectors:

            name = selector.xpath(".//span[@class='title']/text()").extract()
            name = name[0]
            xiangqing = selector.xpath(".//div[@class='bd']/p/text()[2]").extract()
            xiangqing = xiangqing[0].strip()
            index2 = xiangqing.find('/', xiangqing.find('/', 2)+1)
            juqing = xiangqing[index2+1:]
            year = re.findall('(.*?)/', xiangqing)[0].strip()
            city = re.findall('(.*?)/', xiangqing)[1].strip()
            zhiyuan = selector.xpath(".//div[@class='bd']/p/text()[1]").extract()
            zhiyuan = zhiyuan[0].strip()
            index1 = zhiyuan.find(':', 1)
            index2 = zhiyuan.find('主', 1)
            index3 = zhiyuan.find(':', index1+1)
            daoyan = zhiyuan[index1+1:index2]
            zhuyan = zhiyuan[index3+1:]
            pinglun = selector.xpath('.//div[@class="star"]/span[4]/text()').extract()
            link = selector.xpath(".//div[@class ='hd']/a/@href").extract()
            pingfen = selector.xpath('.//div[@class="star"]/span[2]/text()').extract()
            items = {
                            '电影名': name,
                            '电影链接': link,
                            '上映时间': year,
                            '上映城市': city,
                            '剧情': juqing,
                            '导演': daoyan,
                            '主演': zhuyan,
                            '豆瓣评分':pingfen
                        }
            const_item['name'] = name
            const_item['link'] = link
            yield const_item
            # print(const_item)