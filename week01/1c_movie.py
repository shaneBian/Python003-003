import requests
import lxml.etree

# 爬取页面详细信息

# 电影详细页面
#url = 'https://movie.douban.com/subject/1292052/'
url = 'https://maoyan.com/films/3606'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
Cookie = '121484983.1597841518129.1597844249273.1597844250798.5; uuid_n_v=v1; uuid=C341FC10E21A11EAB90FBBC3BB80078A71AF5CE900C3436A9B2B94DC6F5A35C3; _csrf=a6c57c2d1d338f5217472e4ac70365e15f1c07d6d731ff943af34fe3b58ff58b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597841517; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597844251; _lxsdk_cuid=17406c6ac06c8-06a4ac0ea6603b-4b5a61-fa000-17406c6ac0691; _lxsdk_s=17406c6ac07-c35-ca6-dac%7C%7C13; _lxsdk=C341FC10E21A11EAB90FBBC3BB80078A71AF5CE900C3436A9B2B94DC6F5A35C3; __mta=121484983.1597841518129.1597843138669.1597843483369.4; mojo-uuid=a5e733a03ae2beed437acbbcaa0373fd; mojo-trace-id=10; mojo-session-id={"id":"2595e2c611e2c2b951656719b2874027","time":1597841518299}'
# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
header['Cookie'] = Cookie
response = requests.get(url, headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)
#print(response.text)
# 电影名称
#film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
print(f'电影名称: {film_name}')

# 上映日期
#plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
print(f'上映日期: {plan_date}')

# 评分
#rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
rating = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@class="text-link"]/text()')
print(f'评分：{rating}')

mylist = [film_name, plan_date, rating]


import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

