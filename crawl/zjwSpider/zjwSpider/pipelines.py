# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql
import pymssql
from sqlalchemy import create_engine
import pandas as pd
class ZjwspiderPipeline(object):
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
        a1 = item['ProjectName']
        a2 = item['ProjectNumber']
        a3 = item['VendorName']
        a4 = item['VendorContact']
        a5 = item['VendorPM']
        a6 = item['ContractType']
        a7 = item['ContractSize']
        a8 = item['ContractCounty']
        a9 = item['ContractorName']
        a10 = item['ContractorContact']
        a11 = item['ContractorPM']
        a12 = item['ContractDate']
        a13 = item['ContractAmount']
        a14 = item['ContractAddress']
        # if a1 not in df.values:
        self.cursor.execute("INSERT INTO dbo.SalesLeads_Contract(ProjectName,ProjectNumber,VendorName,VendorContact,\
                                VendorPM, ContractType,ContractSize ,ContractCounty,ContractorName, ContractorContact, ContractorPM,\
                                ContractDate ,ContractAmount, ContractAddress,TypeID,IsEnabled)VALUES ('{}','{}','{}','{}','{}','{}','{}',\
                                '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,3,1))
        self.conn.commit()
    def close_spider(self, spider):
        print('爬虫结束!')
