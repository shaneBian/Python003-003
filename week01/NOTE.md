学习笔记

scrapy基本配置点：
1.settings.py配置文件，使用pipe时需要将此处的注释解放出来
    ITEM_PIPELINES = {
    'doubanmovie.pipelines.DoubanmoviePipeline': 300,
    }

2.pandas与csv在操作读写时有什么区别？
