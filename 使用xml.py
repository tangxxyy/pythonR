from lxml import etree
import requests
url = 'http://www.itheima.com/'
answer = requests.get(url)
answer.encoding = 'UTF-8'
# print(answer.text)
# 转换格式
html = etree.HTML(answer.text)
divs = html.xpath("/html/body/div[2]/div[11]/div/div[3]/div[1]/div[2]/ul[1]/li")
for div in divs:
    a = div.xpath("./div[2]/h2/text()")
    print(a)

