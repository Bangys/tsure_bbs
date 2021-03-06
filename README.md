<h1 align="center">TSure BBS</h1>
<p align="center">
  <a href="https://github.com/Bangys/tsure_bbs">
    <img alt="tsure" src="https://github.com/Bangys/tsure_bbs/blob/master/app/static/p1.png" width="140">
  </a>
</p>
<p align="center">一个进化的Web App</p>

<p align="center">
  <a href="https://github.com/Bangys/tsure_bbs/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-brightgreen.svg"></a>
  <a href="https://github.com/Bangys"><img src="https://img.shields.io/badge/developing%20with-Bangys-blue.svg"></a>
  <a href="https://github.com/Bangys/tsure_bbs"><img src="https://img.shields.io/badge/version-v0.2-red.svg"></a>
</p>

---

## 简介
一个Python3+Flask搭建的样式偏冷系的论坛系统，具备基本功能:登陆/注册/发帖/评论，侧边栏菜单、首页轮播图，后续会加入更多工具类的功能

### 界面
<p align="center">
  <img src="https://github.com/Bangys/tsure_bbs/blob/master/app/static/show1.jpg">
  <img src="https://github.com/Bangys/tsure_bbs/blob/master/app/static/show2.jpg">
  <img src="https://github.com/Bangys/tsure_bbs/blob/master/app/static/show3.jpg">
</p>


## 使用
### 依赖环境
在目录下使用pip安装`pip install -r requirements.txt`, 建议在虚拟环境下安装
```
certifi==2019.3.9
chardet==3.0.4
Click==7.0
cssselect==1.0.3
dominate==2.3.5
Flask==1.0.3
Flask-Bootstrap==3.3.7.1
Flask-SQLAlchemy==2.4.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
lxml==4.3.3
MarkupSafe==1.1.1
PyMySQL==0.9.3
pyquery==1.4.0
requests==2.22.0
selenium==3.141.0
SQLAlchemy==1.3.4
urllib3==1.25.3
visitor==0.1.3
Werkzeug==0.15.4
```
### 配置文件
需要配置数据库地址, 在根目录下的`config.py`中, 替换`SQLALCHEMY_DATABASE_URI`：
```
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '435hiud6gdb73bsjh^&G&^fg3bh*&GH'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT = 'your salt'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/tsure'


config = {
    'default': DevelopmentConfig
}


```
### 启动
在根目录下运行
```
python run.py
```

## 版本记录
### v0.2 
`2019-06-03`

- 新增
  - 数据抓取：豆瓣、VGtime
  - 首页轮播图、九宫格布局
  
- 修改
  - 整体布局样式
  - 加入部分CSS3动画

### v0.1
`2019-05-19`
- 页面部分
  - 首页 index
  - 文章详情页 detail
  - 文章编辑页 edit
  - 个人页 profile

### 
- 数据模型

  - 文章 Post
  - 用户 User
  - 评论 Comment
  - 板块 Board

### 
- 主要逻辑
  - 首页获取全部文章页
  - 文章的添加、删除
  - 用户和文章的关联、文章与板块、评论与用户和文章的关联
  - 文章对应板块
