# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ClimbPipeline(object):

    def process_item(self, item, spider):

        print("电影排名：{0}".format(['rank'][0]))

        print("电影名字：{0}".format(['name'][0]))

        print("评分：{0}".format(['king'][0]))

        return item
