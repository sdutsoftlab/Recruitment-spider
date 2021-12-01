"""
1、目的 下载所有的英雄皮肤图片
2、分析网页
    1、找寻所有英雄
    2、查看单个英雄皮肤内容
    3、根据英雄皮肤的页面 进行分析接口（皮肤的接口是通过英雄的id进行加载）
        https://game.gtimg.cn/images/lol/act/img/js/hero/1.js?ts=2729565
"""
import requests
import time
import os


# 保存文件的方法
def save_img(data, roles, filename):
    for role in roles:
        path = './img/{}/'.format(role)
        if not os.path.exists(path):
            os.makedirs(path)

        filename = filename.replace('/', '\\')  # K/DA 伊芙琳.jpg 路径问题
        # data是图片的二进制流
        with open('{}{}.jpg'.format(path, filename), 'wb') as file:
            file.write(data)
            print('{}{}.jpg 图片下载成功！'.format(path, filename))


# 访问提取单个英雄的皮肤  roles：皮肤分类
def get_hero_skins(heroId, roles):

    url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2729565".format(
        heroId)
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    res = requests.get(url, headers=hd)
    data = res.json()
    skins = data['skins']
    for skin in skins:
        # print(skin)
        mainImg = skin['mainImg']
        heroName = skin['name']
        if mainImg:
            print(mainImg)
            img_res = requests.get(mainImg)
            # 保存文件
            save_img(img_res.content, roles, heroName)


# 获取所有的英雄id
def get_hero_ids():
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2729567"
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    res = requests.get(url, headers=hd)
    data = res.json()
    heros = data['hero']
    for hero in heros:
        # hero是个字典
        heroId = hero['heroId']
        roles = hero['roles']  # 角色
        print(heroId,  '='*100)
        get_hero_skins(heroId, roles)
        time.sleep(1)  # 强制等待1秒


get_hero_ids()

# get_hero_skins()
