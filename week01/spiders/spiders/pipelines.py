# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        with open('./maoyan.csv', "a+", newline='') as file:
            csv_file = csv.writer(file)
            csv_file.writerow([film_name, film_type, plan_date])
        return item
