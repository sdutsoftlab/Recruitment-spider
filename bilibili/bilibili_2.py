
"""
1、网页源代码中 包含了视频的下载链接
2、moviepy这个模块 合并视频和音频


安装模块
    pip install moviepy
"""
import requests
import json
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip, AudioFileClip


def save_file(obj, filename, otype):
    """
    :param obj:  # 请求获取的对象
    :param filename:  保存的文件名称
    :param otype:  保存的文件后缀
    :return:
    """
    with open('{}.{}'.format(filename, otype), 'wb') as f:
        f.write(obj.content)
        print('{}保存成功!'.format(filename))


def requests_get(url, hd):
    return requests.get(url, headers=hd)


base_url = "https://www.bilibili.com/video/BV19U4y1K7yz"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
    "referer": "https://live.bilibili.com/"
}
res = requests_get(base_url, headers)
soup = BeautifulSoup(res.text, 'html.parser')
script_list = soup.find_all('script')
for script in script_list:
    text = script.text
    if '__playinfo__' in text:
        print(text)
        replace_res = text.replace('window.__playinfo__=', '')
        print(replace_res)
        data = json.loads(replace_res)
        print(data)
        video = data['data']['dash']['video'][0]['baseUrl']  # 视频链接
        audio = data['data']['dash']['audio'][0]['baseUrl']  # 音频链接
        print(video)
        print(audio)

        # 请求下载视频
        # 视频的清晰度   超清 4k   标清 1080p
        video_param = {
            "accept_description": "超清 4K",
            "accept_quality": "120"
        }
        # 视频的请求
        video_res = requests.get(video, headers=headers, params=video_param)

        # 音频的请求
        audio_res = requests.get(audio, headers=headers)

        # 保存到文件里
        print('正在下载视频')
        save_file(video_res, '视频文件', 'mp4')
        print('正在下载音频')
        save_file(audio_res, '音频文件', 'mp3')

        print('开始合并音视频...')
        # 合并音频、视频
        # 刚才保存的视频文件
        v_path = './视频文件.mp4'
        a_path = './音频文件.mp3'

        # 创建视频的合并对象
        videoclip = VideoFileClip(v_path)
        # 创建音频的合并对象
        audioclip = AudioFileClip(a_path)

        # 将音频文件对象，写入到视频对象中，
        clip_res = videoclip.set_audio(audioclip)
        # 需要有一个写出保存
        clip_res.write_videofile('合并之后的文件.mp4')
        print('合并成功！')

    # print('='*200)
