# coding:utf-8
import configparser
import os
# cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件路径
cur_path = os.path.abspath(os.path.join(os.getcwd()))
cfg_path = os.path.join(cur_path,'config\config.ini')

conf = configparser.ConfigParser()
conf.read(cfg_path)

# 读取服务器配置
sql_host = conf.get('sql_info','host')
sql_uer = conf.get('sql_info','user')
sql_port = conf.get('sql_info','port')
sql_password = conf.get('sql_info','password')
sql_db = conf.get('sql_info','db')
sql_charset = conf.get('sql_info','charset')

# 读取浏览器配置
browserName = conf.get('browserType','browserName')

# 读取测试url
url = conf.get('testServer','url')
