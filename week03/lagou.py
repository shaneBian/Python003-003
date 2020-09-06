from selenium import webdriver
import time
import lxml.etree
import threading
import pymysql

threads = []
jobInfo = []
info_set = set()
dbInfo = {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            'password' : '52Tutu@mysql',
            'db' : 'spiderDB'
        }

class MyThread(threading.Thread):
    def __init__(self, n, city):
        super().__init__() 
        self.n = n
        self.city = city

    def run(self):
        global jobInfo
        global info_set
        option=webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        #browser = webdriver.Chrome()
        browser.get(f'https://www.lagou.com/{self.city}-zhaopin/Python/{self.n}/')
        time.sleep(1)

        selector = lxml.etree.HTML(browser.page_source)
        for tags in selector.xpath('//li[@class="con_list_item default_list"]'):
            job_salary = tags.xpath('./@data-salary')[0].strip().split('k')[0]
            job_name = tags.xpath('./@data-positionname')[0].strip()
            info = f'{job_salary}{job_name}{self.city}'  ##使用set去重
            if info not in info_set:
                info_set.add(info)
                jobInfo.append([job_name, job_salary, f'{self.city}'])

        browser.close()



if __name__ == '__main__':
    for i in range(24):
        bj = MyThread(i, "beijing")
        threads.append(bj)
        bj.start()
 
    for i in range(24):
        sh = MyThread(i, "shanghai")
        threads.append(sh)
        sh.start()

    for i in range(24):
        sz = MyThread(i, "shenzhen")
        threads.append(sz)
        sz.start()
 
    for i in range(24):
        gz = MyThread(i, "guangzhou")
        threads.append(gz)
        gz.start()
    for j in threads:
        j.join()

    conn = pymysql.connect(
        host = dbInfo['host'],
        port = dbInfo['port'],
        user = dbInfo['user'],
        password = dbInfo['password'],
        db = dbInfo['db']
    )
    cur = conn.cursor()
    for job in jobInfo:
        sqlCommand = f'insert into job_info VALUES ("{job[0]}", "{job[1]}", "{job[2]}")'
        try:
            cur.execute(sqlCommand)
            conn.commit()
        except:
            conn.rollback()
    cur.close()
    conn.close()
