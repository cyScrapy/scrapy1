# import sys, pymysql
#
#
#
# try:
#     db = pymysql.connect('localhost', 'root', '1206', 'cy', charset='utf8')
#
# except:
#     print("db Link error")
#
# else:
#
#     print('link success')
# import pymysql.cursors
#
# #连接数据库
# connect = pymysql.connect(
#     host = 'localhost',  #服务器的IP地址 本地的填localhost
#     port = 3306,              #mysql端口 一般为3306
#     user = 'root',           #账号
#     passwd = '1206',     #密码
#     db = 'cy' ,              #数据库名称
#     charset = 'utf8'
# )
# print("link success")
#
# #获取游标
# cursor = connect.cursor()
#
# #插入数据
# cursor.execute("insert into cy.rfid(card_id,user) values('201','sanpang')")
# print('insert success')
#
# #查询数据
# cursor.execute("select * from cy.rfid")
# for raw in cursor.fetchall():
#     print("%s%s%s%s"%(card_id,user,flag,time))

# #关闭连接
# cursor.close()
# connect.close()