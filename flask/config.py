import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    #格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zong123456@localhost:3306/flaskblog?charset=utf8'
    #如果你不打算使用mysql，使用这个连接sqlite也可以
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #设置密匙要没有规律，别被人轻易猜到哦
    SECRET_KEY = 'MYSECRETKEY'

article_list = [
    {'title': '浏览器如何识别selenium及爬虫如何绕过反爬', 'url': 'https://zhuanlan.zhihu.com/p/78368287', 'look': 'None', 'useful': '23'}, 
    {'title': 'js加密中遇到document/window属性怎么办？', 'url': 'https://zhuanlan.zhihu.com/p/77779698', 'look': 'None', 'useful': '2'}, 
    {'title': 'scrapy的去重与过滤器的使用', 'url': 'https://zhuanlan.zhihu.com/p/79120407', 'look': 'None', 'useful': '4'}, 
    {'title': '异步/分布式爬虫的常见库及优缺点总结', 'url': 'https://zhuanlan.zhihu.com/p/80299778', 'look': 'None', 'useful': '2'}, 
    {'title': '从细节上提高爬虫的运行效率', 'url': 'https://zhuanlan.zhihu.com/p/81343456', 'look': 'None', 'useful': '5'}
]