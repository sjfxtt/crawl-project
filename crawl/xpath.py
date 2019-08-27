#导入工具
import requests
res = requests.get("http://www.bcactc.com/home/gcxx/now_sgzbgg.aspx")
res.text
#lxml是一个专门用于解析xml语言的库
from lxml import etree
response = etree.HTML(res.text)
values = response.xpath('//div[@style="float:right"]/text()[1]')[0].strip()
