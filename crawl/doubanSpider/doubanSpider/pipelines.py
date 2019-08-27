# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv
class DoubanspiderPipeline(object):
    def __init__(self):
        store_file = os.path.dirname(__file__) + '/spiders/data.csv'
        self.file = open(store_file, 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file, dialect="excel")
    def process_item(self, item, spider):
        self.writer.writerow([item['name'], item['link']])
        return item

    def close_spider(self, spider):
        self.file.close()
