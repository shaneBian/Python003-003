学习笔记
文档说明：
猫眼电影网址： https://maoyan.com/films?showType=3
作业一：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
【答案】：./requests_bs4.py


作业二：
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
【答案】：./spiders


scrapy基本配置点：
1.settings.py配置文件，使用pipe时需要将此处的注释解放出来
    ITEM_PIPELINES = {
    'doubanmovie.pipelines.DoubanmoviePipeline': 300,
    }

2.pandas与csv在操作读写时有什么区别？
