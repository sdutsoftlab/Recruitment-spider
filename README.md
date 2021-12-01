# Recruitment-spider
招聘网站信息爬虫 （前程无忧，拉钩网，人才网，58同城，百姓网）

* [bilibili](./bilibili)
* [京东](./jd)
* [LOL皮肤](./lol)
* [网易云](./wangyiyun)
* [链家](./lianjias)

#### 开发工具

scrapy爬虫框架+mysql8.0+pycharm

#### 开发技术

cv+csdn

#### 运行环境

windows10+scrapy0.7.2+python3



项目结构

```
|——— folder  #项目目录
	|——— spider  #爬虫脚本目录，可以有多个脚本
	|    |——— spider.py #爬虫脚本
	|——— __init__.py #空文件，没个蛋用
	|——— items.py         #定义保存内容
	|——— middlewares.py   #中间件，可添加请求表头和ip代理
	|——— pipelines.py     #处理item并保存数据库
	|——— settings.py       #项目配置文件，可定义爬取速率和数据库配置等
	|——— start.py         #启动文件
	|___ 其他    #一些别的东西可能有用
	
```

```
#命令行启动
cd 项目
scrapy crawl [爬虫名]
```

如图

![image-20200718222124038.png](https://i.loli.net/2020/07/20/RP3DmWfB9QTseJc.png)

运行效果

![image-20200718222210243.png](https://i.loli.net/2020/07/20/ImLV3oGb4CqMlNY.png)
数据库

![image-20200718222439222.png](https://i.loli.net/2020/07/20/WIgTmHDxJ5nPFtX.png)
