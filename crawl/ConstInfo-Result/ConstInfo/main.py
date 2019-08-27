from scrapy import cmdline
print('开始爬虫！')
print('************')
print('************')
# import pymssql
# conn = pymssql.connect(user = 'it.intern',password = 'lsh#123',host = 'sql04.lshmnc.com.cn',database = 'PYTHON_LAB')
# cursor = conn.cursor()
# insert1 = "INSERT INTO python_lab.dbo.T_LOG (PROJECT, ITEM,  STATUS, DESCRIPTION, LOGLEVEL) VALUES ('SalesLeads', 'Python Process Begin', 'DONE', '', 'INFO');COMMIT"
# cursor.execute(insert1)
# conn.rollback()
# cursor.close()
# conn.close()
cmdline.execute('scrapy crawl const_spider'.split())
