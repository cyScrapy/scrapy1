# import os
# import time
# import json
#
# class ClimbPipeline(object):
#     def __init__(self):
#         self.file_name='outdata'
#         if not os.path.exists(self.file_name):
#             os.mkdir(self.file_name)
#             pass
#         #
#         # current_time=time.strftime('%Y-%m-%d-%H',time.localtime())#-%M
#         self.file_name=self.file_name+os.sep+'donbanmovie_top'+'.json'
#
#
#     def process_item(self, item, spider):
#         with open("self.file_name", "a") as fp:
#
#             json.dump(self.file_name, fp)
#
#         print("加载入文件完成...")
#         # with open("self.file_name", 'a', encoding='utf-8') as fp:
#
#         # with open(self.file_name,'a',encoding='utf-8') as fp:
#         #     fp.write('rank:%s\t'%item['rank'][0])
#         #     fp.write('name:%s\t'%item['name'][0])
#         #     fp.write('king:%s\t'%item['king'][0])
#         #     fp.write('pic:%s '%item['pic'][0])
#         #     fp.write('dir:%s '%item['dir'][0])
#         #     fp.write('intro:%s'%item['intro'][0])
#         #     fp.write('\n')