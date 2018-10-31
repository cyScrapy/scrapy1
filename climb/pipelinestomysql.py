# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ClimbPipeline(object):

    def process_item(self, item, spider):
        db=pymysql.connect('localhost', 'root', '1206', 'cy', charset='utf8')

        cur=db.cursor()
        # cur.execute('set name utf8')

        rank=item['rank'][0]    # .encode('ascii').decode('utf8')
        name = item['name'][0]    # .encode('ascii').decode('utf8')
        # print('---------------------------', name.encode(), '---------------------------\n')
        king=item['king'][0]    # .encode('ascii').decode('utf8')
        pic= item['pic'][0]    # .encode('ascii').decode('utf8')
        dir =item['dir'][0]    # .encode('ascii').decode('utf8')
        intro=item['intro'][0]    # .encode('ascii').decode('utf8')

        sql="insert into douban1 values(%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,((int)(rank),name,king,pic,dir,intro))
        db.commit()

        if cur:
            cur.close()


        return item
# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
#
#
# # 指定数据输出方式
# class DoubanmoviePipeline(object):
#     def process_item(self, item, spider):
#         # 获取连接
#         db = pymysql.connect('localhost', 'root', '1205', '')
#         # 获取数据库操作对象
#         cur = db.cursor()
#         # 设置字符集编码方式
#         cur.execute('set names utf8;')
#         # 获取爬取的数据
#         rank = item['rank'][0]
#         title = item['name'][0]
#         url = item['pic'][0]
#         scr = item['scr'][0]
#
#         sql = "insert into douban values(%s,%s,%s,%s)"
#         # 执行SQL语句
#         cur.execute(sql, ((int)(rank), title, url, scr))
#         # 提交
#         db.commit()
#
#         # 关闭游标
#         if cur:
#             cur.close()
#
#         return item
