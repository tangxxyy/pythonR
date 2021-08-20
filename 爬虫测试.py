# 找到tx视频的电影列表
import re
from urllib.request import urlopen
import csv
url = 'https://v.qq.com/channel/movie?listpage=1&channel=movie&sort=18&_all=1'
# 打开了网页
head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 "
                  "UBrowser/6.2.4098.3 Safari/537.36 "
}
# 得到网页源代码
# 使用requests的问题，打开网页源代码的时候出现乱码
answer = urlopen(url)
# print(answer.read().decode())
sc = answer.read().decode()
# 设置预定义的正则表达式进行提取信息
predefine = re.compile(r'<div class="list_item" __wind>.*?<div class="figure_caption" >(?P<time>.*?)</div>.*?'
                       r'<div class="figure_score">(?P<score>.*?)</div>.*?'
                       r'<a href=.*?>(?P<name>.*?)</a>.*?'
                       r'</svg>(?P<all>.*?)</div>', re.S)
a = predefine.finditer(sc)
for i in a:
    print("电影名字：", i.group("name"))
    print("电影时间：", i.group("time"))
    print("电影评分：", i.group("score"))
    print("电影票房：", i.group("all"))
    print('\r')