# -*- coding: utf-8 -*-
import scrapy


class CyspiderSpider(scrapy.Spider):
    name = 'cyspider'
    allowed_domains = ['xiaozhu.com']
    start_urls = ['http://xiaozhu.com/']

    def parse(self, response):
        pass
