# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i = 0
        for movie in movies:
            if i > 9:
                break
            item = SpidersItem()
            film_name = movie.xpath('./div[1]/span/text()')
            film_type = movie.xpath('./div[2]/text()')
            plan_date = movie.xpath('./div[4]/text()')
            item['film_name'] = film_name.extract()[0].strip()
            item['film_type'] = film_type.extract()[1].strip()
            item['plan_date'] = plan_date.extract()[1].strip()
            i = i + 1
            yield item