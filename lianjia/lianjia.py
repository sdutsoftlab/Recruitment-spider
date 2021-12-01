"""
链家网的详细信息

1、目的：爬取房源信息
    房源的标题
    位置
    户型
    总价
    单价/平米

2、链接  https://zz.lianjia.com/ershoufang/rs%E5%B0%8F%E5%8C%BA/
3、分析是否静态或动态页面
4、针对性标签定位

"""
import time
import csv
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

# url编码
# wd = '小区'
# res = quote(wd)
# print(res)


class LianJia():
    def __init__(self):
        self.base_url = "https://zz.lianjia.com/ershoufang/pg{}rs{}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
        }

        file = open('链家网.csv', 'w', encoding='utf-8-sig', newline='')
        self.csv_file = csv.writer(file)
        self.csv_file.writerow(['房源名', '地理位置', '户型朝向', '总价', '单价'])

    def requests_get(self, url, headers):
        # 请求
        return requests.get(url, headers=headers)

    def parse(self, html):
        # 进行解析提取数据
        soup = BeautifulSoup(html, 'html.parser')

        div_list = soup.find_all('div', attrs={"class": "info clear"})
        for div in div_list:
            # print(div)
            # 获取名称标题
            title = div.find('div', attrs={"class": "title"}).find('a').string
            print(title)
            # 获取位置
            positionInfo = div.find(
                'div', attrs={"class": "positionInfo"}).text.strip()
            print(positionInfo)
            # 获取房间信息
            houseInfo = div.find('div', attrs={"class": "houseInfo"}).text
            print(houseInfo)
            # 获取总价
            totalprice = div.find(
                'div', attrs={"class": "totalPrice totalPrice2"}).text.strip()
            print(totalprice)
            # 获取单价
            unitPrice = div.find('div', attrs={"class": "unitPrice"}).text
            print(unitPrice)

            self.csv_file.writerow([
                title,
                positionInfo,
                houseInfo,
                totalprice,
                unitPrice
            ])
            print('='*200)

    def run(self):
        # 启动函数

        for page in range(1, 10):
            url = self.base_url.format(page,  quote('小区'))
            # 请求链接
            res = self.requests_get(url, self.headers)
            self.parse(res.text)
            time.sleep(1)


LianJia().run()
