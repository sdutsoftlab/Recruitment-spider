"""
1、目标 爬取b站视频
2、 接口链接
    https://api.bilibili.com/x/player/playurl?cid=449887968&otype=json&bvid=BV1QL4y1p7EA

3、获取cid和 bvid
4、请求的时候需要携带  referer
"""

import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# https://www.bilibili.com/video/BV18M4y1P7Qq?from=search&seid=17978592583277174073&spm_id_from=333.337.0.0


class BSpider():
    def __init__(self):
        self.base_url = "https://api.bilibili.com/x/player/playurl?cid={}&otype=json&bvid={}"

    def selenium_parse(self, url):
        # selenium进行访问获取参数
        driver = webdriver.Chrome(
            executable_path='/Users/devhg/chromedriver')
        driver.get(url)
        time.sleep(1)
        playerInfo = driver.execute_script('return window.playerInfo')
        print(playerInfo)
        html = driver.page_source
        driver.quit()
        return playerInfo, html

    def requests_get(self, url):
        # 请求视频信息的链接
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
            "referer": "https://live.bilibili.com/"
        }
        return requests.get(url, headers=headers)

    def save_file(self, content, filename):
        with open('{}.mp4'.format(filename), 'wb') as f:
            f.write(content)

    def get_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string

    def run(self):
        # 启动入口
        url = input("请输入视频链接：")
        playerInfo, html = self.selenium_parse(url)
        video_info_url = self.base_url.format(
            playerInfo['cid'], playerInfo['bvid'])
        res = self.requests_get(video_info_url)  # 获取视频详情的链接
        data = res.json()['data']
        durl = data['durl'][0]['url']  # 提取视频下载链接
        down_res = self.requests_get(durl)  # 获取下载链接对象
        filename = self.get_title(html)  # 获取网址中的title 用作下载视频的名字
        self.save_file(down_res.content, filename)


BSpider().run()
