from scrapy import cmdline
# import sys
# import os

# dirpath = os.path.dirname(os.path.abspath(__file__))
# print(dirpath)
# # 添加环境变量
# sys.path.append(dirpath)
# # 启动爬虫,第三个参数为爬虫name
# execute(['scrapy','crawl','qcwy'])

cmdline.execute("scrapy crawl qcwy".split())