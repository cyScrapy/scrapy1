# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import JianshuItem
from scrapy.http import Request

class CyspiderSpider(scrapy.Spider):
    name = 'cyspider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/recommendations/collections?page=1&order_by=hot']

    def parse(self, response):
        item=JianshuItem()
        selector=Selector(response)
        infos=selector.xpath('//div[@class="col-xs-8"]')
        for info in infos:
            try:
                name=info.xpath('div/a/h4/text()').extract()[0]
                content=info.xpath('div/a/p/text()').extract()[0]
                article = info.xpath('div/div/a/text()').extract()[0]
                fans = info.xpath('div/div/text()').extract()[0]

                item['name']=name
                item['content'] =content
                item['article'] =article
                item['fans'] =fans

                yield item

            except:
                pass

        urls=['https://www.jianshu.com/recommendations/collections?page={0}&order_by=hot'.format(str(i)) for i in range(1,10)]

        for url in urls:

            yield Request(url,callback=self.parse)





