# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import PigWebItem

class CyspiderSpider(scrapy.Spider):
    name = 'cyspider'
    allowed_domains = ['xiaozhu.com']
    start_urls = ['http://xm.xiaozhu.com/fangzi/4499245414.html']

    def parse(self, response):

        item=PigWebItem()
        selector=Selector(response)
        title=selector.xpath('//div[1]/h4/em/text()').extract()[0]
        address=str(selector.xpath('//div[1]/p/span[@class="pr5"]/text()').extract()[0]).strip()
        price=selector.xpath('//*[@id="pricePart"]/div[1]/span/text()').extract()[0]
        house=selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
        rank=selector.xpath('//div[1]/ul[3]/li[3]/em/text()').extract()[0]
        bed=selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]
        module=selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]

        item['address']=address
        item['title']=title
        item['price']=price
        item['house']=house
        item['rank']=rank
        item['bed']=bed
        item['module']=module

        yield item
