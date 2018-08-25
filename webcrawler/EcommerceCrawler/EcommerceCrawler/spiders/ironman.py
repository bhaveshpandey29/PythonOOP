# -*- coding: utf-8 -*-
import scrapy


class IronmanSpider(scrapy.Spider):
    name = 'ironman'
    allowed_domains = ['https://www.amazon.in/']
    start_urls = ['https://www.amazon.in//']

    def parse(self, response):
        f=open('demo.html','w+')
        for i in response.xpath("//img/@src").extract():
            f.write(f"<img src='{str(i)}'/>")
