# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql
import pymssql
from sqlalchemy import create_engine
import pandas as pd

class Test1SpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'sql04.lshmnc.com.cn',
            'user': 'it.intern',
            'password':'lsh#123',
            'database':'PYTHON_LAB'
        }
        self.conn = pymssql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    def process_item(self,item,spider):
        engine = create_engine('mssql+pymssql://it.intern:lsh#123@sql04.lshmnc.com.cn:1433/PYTHON_LAB')
        # df = pd.read_sql("select ProjectNumber from dbo.SalesLeads_Bidding", engine)
        # print(df)
        print(item)
        a1 = item['ProjectNumber']
        a2 = item['ProjectName']
        a3 = item['ProjectLocation']
        a4 = item['ProjectSize']
        a5 = item['BiddingBudget']
        a6 = item['BiddingScope']
        a7 = item['BiddingCompany']
        a8 = item['BiddingContact']
        a9 = item['BiddingAddress']
        a10 = item['BiddingContactTel']
        a11 = item['BiddingAgencyCompany']
        a12 = item['BiddingAgencyAddress']
        a13 = item['BiddingAgencyContact']
        a14 = item['BiddingAgencyContactTel']
        a15 = item['BiddingEndDate']
        # if a1 not in df.values:
        self.cursor.execute("INSERT INTO dbo.SalesLeads_Bidding(ProjectNumber, ProjectName,ProjectLocation,ProjectSize,\
                                BiddingBudget,BiddingScope,BiddingCompany, BiddingContact,BiddingAddress,\
                                BiddingContactTel,BiddingAgencyCompany,BiddingAgencyAddress,BiddingAgencyContact,\
                                BiddingAgencyContactTel,BiddingEndDate,TypeID,IsEnabled)VALUES ('{}','{}','{}','{}','{}','{}','{}',\
                                '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,2,1))
        self.conn.commit()
    def close_spider(self, spider):
        print('爬虫结束!')