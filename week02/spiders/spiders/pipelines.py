# -*- coding: utf-8 -*-
import csv
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class SpidersPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        #with open('./maoyan.csv', "a+", newline='') as file:
        #   csv_file = csv.writer(file)
        #    csv_file.writerow([film_name, film_type, plan_date])

        dbInfo = {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            'password' : '52Tutu@mysql',
            'db' : 'spiderDB'
        }
        sqlCommand = 'insert into maoyan_movie VALUES ("'+film_name+'", "'+film_type+'", "'+plan_date+'")'
        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
        )
        cur = conn.cursor()
        try:
            cur.execute(sqlCommand)
            #关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()
        return item
