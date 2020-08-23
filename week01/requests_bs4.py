# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装

movie_list = []
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
Cookie = '__mta=121484983.1597841518129.1597853249732.1597854064519.13; uuid_n_v=v1; uuid=C341FC10E21A11EAB90FBBC3BB80078A71AF5CE900C3436A9B2B94DC6F5A35C3; _csrf=a6c57c2d1d338f5217472e4ac70365e15f1c07d6d731ff943af34fe3b58ff58b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597841517; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597854224; _lxsdk_cuid=17406c6ac06c8-06a4ac0ea6603b-4b5a61-fa000-17406c6ac0691; _lxsdk=C341FC10E21A11EAB90FBBC3BB80078A71AF5CE900C3436A9B2B94DC6F5A35C3; __mta=121484983.1597841518129.1597854064519.1597854224024.14; mojo-uuid=a5e733a03ae2beed437acbbcaa0373fd; _lxsdk_s=1740779ad29-0b-38c-2db%7C%7C9; mojo-trace-id=4; mojo-session-id={"id":"6f1008eb54c81f361317fa8f06cf2ce5","time":1597853249500}'
Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
Accept_Language = 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
Cache_Control = 'max-age=0'
Connection = 'keep-alive'
Host = 'maoyan.com'
Upgrade_Insecure_Requests = '1'

header = {'user-agent':user_agent,'Cookie':Cookie,'Accept':Accept,'Accept-Language':Accept_Language,'Cache-Control':Cache_Control,'Connection':Connection,'Host':Host,'Upgrade-Insecure-Requests':Upgrade_Insecure_Requests}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
#print(response.text)
bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
i = 0
for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
    movieUrl = "https://maoyan.com" + tags.find('a').get('href')  
    movieResponse = requests.get(movieUrl,headers=header)
    movie_info = bs(movieResponse.text, 'html.parser')
    film_name = movie_info.find('h1', attrs={'class': 'name'}).text
    film_type = movie_info.find_all('li', attrs={'class': 'ellipsis'})[0].text
    plan_date = movie_info.find_all('li', attrs={'class': 'ellipsis'})[2].text
    
    movie_list.append([film_name, film_type, plan_date])
    i = i + 1
    if i > 9:
        break

import pandas as pd

movie_data = pd.DataFrame(data=movie_list)
movie_data.to_csv('./movie.csv', encoding='utf8', index=False, header=False)



