# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PigWebPipeline(object):
    def process_item(self, item, spider):
        f=open('/home/cy/PycharmProjects/10-23demo/pig_web/pig.text','w+')
        f.write("address:"+item['address']+'\n')
        f.write("title:"+item['title']+'\n')
        f.write("price:"+item['price'] + '\n')
        f.write("house:"+item['house'] + '\n')
        f.write("rank:"+item['rank']+'\n')
        f.write("bed:"+item['bed']+'\n')
        f.write("module:"+item['module']+'\n')
        return item
        f.close()