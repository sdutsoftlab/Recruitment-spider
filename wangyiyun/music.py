"""
网易云音乐下载

"""

import requests
from bs4 import BeautifulSoup


# 指定访问链接
url = "https://music.163.com/artist?id=11127"  # 歌手主页的链接，里面有50首歌曲
# 请求头
hd = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
res = requests.get(url, headers=hd)
# print(res.text)
html = res.text

# 创建soup对象
soup = BeautifulSoup(html, 'html.parser')
# span标签得到的内容为空
# span_all = soup.find_all('span', attrs={"class":"txt"})
# for span in span_all:
#     a = span.find('a')
#     print(a)
#     print('='*100)
# ul标签
a_list = soup.find('ul', attrs={"class": "f-hide"}).find_all('a')
for a in a_list:

    # 提取标签中的属性 href
    # 第一种方式提取属性
    href = a['href']
    # 第二种方式提取属性
    # href2 = a.attrs['href']
    # print(href2)
    ids = href[9:]
    # ids = href.split('=')[-1]
    # 歌曲名称
    name = a.text
    song_url = 'https://music.163.com/song/media/outer/url?id=' + ids
    print(song_url)

    # 请求这个歌曲链接，进行保存下载
    song_res = requests.get(song_url)
    with open('./{}.mp3'.format(name), 'wb') as f:
        f.write(song_res.content)
    print('='*100)
