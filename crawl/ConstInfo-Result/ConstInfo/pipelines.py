# -*- coding: utf-8 -*-
import pymssql
import pymssql 
from sqlalchemy import create_engine
import pandas as pd

class ConstinfoPipeline(object):
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
        df = pd.read_sql("select ProjectNumber from SalesLeads_MainItems",engine)
        a1,a2,a3,a4,a5,a6,a7 = item['Number'],item['UnitName'],item['ProjectName'],item['Place'],item['WinningBidder'],item['WinningBidPrice'],item['PublicityStartTime']
        if a1 not in df.values:
            self.cursor.execute("INSERT INTO SalesLeads_MainItems(ProjectNumber, BuildingName\
                    , ProjectName, BuildingLocation,Bidder, BidMoney, OpenDate,TypeID,IsEnabled)\
                        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,a7,1,1))
            self.conn.commit()

    def close_spider(self, spider):
        print('爬虫结束!')