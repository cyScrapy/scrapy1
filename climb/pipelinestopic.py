# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os,time
import urllib
import sys


class ClimbPipeline(object):
    def __init__(self):
        self.folder_name='outdata/images'
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

    def process_item(self, item, spider):

        pic_u = item['pic'][0]

        #数据处理
        file_name=pic_u.split('/')[-1]
        urllib.request.urlretrieve(pic_u,self.folder_name+os.sep+file_name)


        return item
