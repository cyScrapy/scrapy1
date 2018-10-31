# -*- coding: utf-8 -*-
import scrapy
import urllib
import os
import urllib.request
import sys
sys.path.append(r'/home/cy/PycharmProjects/code4/climb/climb')
#from climb.climb.items import ClimbItem
from climb.items import ClimbItem

class CyspiderSpider(scrapy.Spider):
    name = 'cyspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item_list = response.xpath('//div[@class="item"]')
        print(item_list)
        for item in item_list:
                #创建对象
            movie=ClimbItem()

                #读取排名，并保存在实体类中
            movie['rank']=item.xpath('div[@class="pic"]/em/text()').extract()
                # movie['name']=item.xpath('dir[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/test()').extract()

            movie['name']=item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()

            movie['king']= item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"][1]/text()').extract()

            movie['pic'] = item.xpath('div[@class="pic"]/a/img/@src').extract()

            movie['dir'] = item.xpath('div[@class="info"]/div[@class="bd"]/p[1]/text()').extract()

            movie['intro'] = item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[1]/text()').extract()

            yield movie
            #添加对象到生成器中

        nextpage=response.xpath('//span[@class="next"]/a/@href')

        if nextpage:

            url=response.urljoin(nextpage[0].extract())
            #重新请求调用parse
            yield scrapy.Request(url,self.parse)






