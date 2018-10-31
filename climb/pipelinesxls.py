# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import os
# import time
# import xlwt
#
# class ClimbPipeline(object):
#
#
#     def __init__(self):
#
#         self.r=0
#         self.data_list=[]
#
#         self.excelpath=os.path.join(os.getcwd(),'outdata')
#         print(self.excelpath)
#         print(self.excelpath)
#         print(self.excelpath)
#         if not os.path.exists(self.excelpath):
#
#             os.mkdir(self.excelpath)
#             pass
#
#
#
#         self.header=['电影排名','电影名称','评分','图片链接','导演and主演','简介']
#         current_time = time.strftime('%Y-%m-%d-%H',time.localtime())
#         self.file_name = self.excelpath + os.sep + current_time + 'cy_donban.xls'
#
#
#
#
#     def process_item(self, item, spider):
#         self.data_list.append([])
#         self.data_list[self.r].append(item['rank'][0])
#         self.data_list[self.r].append(item['name'][0])
#         self.data_list[self.r].append(item['king'][0])
#         self.data_list[self.r].append(item['pic'][0])
#         self.data_list[self.r].append(item['dir'][0])
#         self.data_list[self.r].append(item['intro'][0])
#         self.r=self.r+1
#
#
#         # self.file_name=self.excelpath+os.sep+current_time+'donban.xls'
#         print(self.file_name)
#
#         self.wokebook = xlwt.Workbook(encoding='utf-8')
#
#         self.sheet=self.wokebook.add_sheet('豆瓣电影排名')
#         for r in range(len(self.header)):
#             self.sheet.write(0,r,self.header[r])
#             for c in range(len(self.data_list)):
#                 self.sheet.write(c+1,r,self.data_list[c][r])
#
#         self.wokebook.save(self.file_name)
#         return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os
import xlrd
import xlwt
from xlutils.copy import copy


class ClimbPipeline(object):
#指定数据输出方式
# class DoubanmoviePipeline(object):
    #构造方法
    def __init__(self):
        self.folder_name='outdata'
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            pass
        #获取当前系统时间
        current_time = time.strftime('%Y-%m-%d-%H',time.localtime())
        #文件的名字
        self.file_name = 'doubanmovie_top250_'+current_time+'.xls'
        #创建文件绝对路径
        self.excelPath = self.folder_name+os.sep+self.file_name
        #创建工作薄
        wb = xlwt.Workbook(encoding='utf-8')

        #创建单页
        sheet = wb.add_sheet('豆瓣电影排名')
        #创建一个标题的列表

        headers = ['电影排名', '电影名称', '评分', '图片链接', '简介','导演and主演']
        #循环写入数据
        for colIndex in range(0,len(headers)):
            sheet.write(0,colIndex,headers[colIndex])
            pass
        #保存工作簿
        wb.save(self.excelPath)
        self.rowIndex = 1
        pass
    def process_item(self, item, spider):
        #打开已创建的excel表
        wb = xlrd.open_workbook(self.excelPath,formatting_info=True)
        #拷贝
        newwb = copy(wb)
        #打开一个单页
        sheet = newwb.get_sheet(0)
        #item转换为列表
        # line = [item['rank'],item['name'],item['pic']]
        line = [item['rank'],item['name'],item['king'],item['pic'],item['intro'],item['dir']]
        for colIndex in range(0,len(item)):
            sheet.write(self.rowIndex,colIndex,line[colIndex])
            pass

        newwb.save(self.excelPath)
        #每个行数加1

        self.rowIndex=self.rowIndex+1

        return item
