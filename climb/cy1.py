# import os
# import time
# import xlwt
#
# #
# # #
# if __name__=="__main__":
#     b.bd()


#
#     pass
#
#     excelpath=os.path.join(os.getcwd(),'outdata')
#     if not os.path.exists(excelpath):
#
#         os.mkdir(excelpath)
#         pass
#
#     file_name=excelpath+os.sep+'data.xls'
#
#     wokebook = xlwt.Workbook(encoding='utf-8')
#
#     sheet=wokebook.add_sheet('豆瓣电影排名')
#
#     header=['电影排名','电影名称','导演','链接']
#
#     for i in range(0,len(header)):
#
#         sheet.write(0,i,header[i])
#
#     for row in range(1,26):
#
#         for col in range(len(header)):
#
#             sheet.write(row,col)
#
#     wokebook.save(file_name)
#
#     print('数据写入完毕')
#

