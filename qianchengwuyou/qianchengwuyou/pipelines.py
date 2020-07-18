# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging
from qianchengwuyou.settings import *
class AbroadwebsitePipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(MYSQL_HOST,MYSQL_ROOT,MYSQL_PASSWORD,MYSQL_DATABASE,charset='utf8',use_unicode=True)
        self.cursor=self.connect.cursor()
        # self.cursor.execute(USE)  # 选定数据库
        self.cursor.execute(DROP)
        self.cursor.execute(CREATE)

    def process_item(self, item, spider):
        try:
            self.cursor.execute(SAVEIN,(item['job_name'],item["salary"],item["degree"],
                            item["experience"],item["category"],item["address"]))
            self.connect.commit()
        except Exception as err:
           logging.error(err)
        return item
    def close_spider(self,spider):
        self.connect.close()

class QianchengwuyouPipeline(object):
    def process_item(self, item, spider):
        return item
