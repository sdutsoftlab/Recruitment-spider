"""
京东案例
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

file = open('京东商品.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer(file)
csv_file.writerow(['商品名称', '商品价格', '商品评价', '商铺名称'])


driver = webdriver.Chrome(executable_path='/Users/devhg/chromedriver')

url = "https://www.jd.com/"
driver.get(url)
time.sleep(1)
# 搜索框并输入
driver.find_element_by_css_selector('#key').send_keys('手机')
# 搜索按钮并点击
driver.find_element_by_css_selector(
    '#search > div > div.form > button > i').click()
time.sleep(3)

while True:
    for i in range(20):
        driver.execute_script('window.scrollBy(0,500);')
        time.sleep(0.1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div_all = soup.find_all('div', attrs={"class": "gl-i-wrap"})
    for div in div_all:
        # 获取价格
        p_price = div.find('div', attrs={'class': "p-price"}).text.strip()
        print(p_price)
        # 获取商品名称
        p_name = div.find(
            'div', attrs={"class": "p-name p-name-type-2"}).em.text.strip()
        print(p_name)
        # 获取评论
        p_commit = div.find('div', attrs={"class": "p-commit"}).text.strip()
        print(p_commit)
        # 获取商铺名称
        shop_name = div.find('div', attrs={"class": "p-shop"}).text.strip()
        print(shop_name)
        print('='*200)

        csv_file.writerow([p_name, p_price, p_commit, shop_name])

    # 进行翻页操作
    try:
        driver.find_element_by_css_selector(
            '#J_bottomPage > span.p-num > a.pn-next').click()
        time.sleep(5)
    except:
        # 当走到这里的时候就是没有下一页，就可以结束程序
        driver.quit()
        break
