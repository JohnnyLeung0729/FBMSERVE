# -*- coding: utf-8 -*-
# @Time : 2022/5/24 18:47
# @Author : qt
# @File : config.py
# @Software: PyCharm
# @contact: 301078114@qq.com
# -*- 功能说明 -*-
# config设定
# 1、数据库设置
# -*- 功能说明 -*-

#数据库设置
USERNAME = "root"
PASSWORD = "Ly818379"
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'fbmtai'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

