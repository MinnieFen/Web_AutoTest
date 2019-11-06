# coding:utf-8
from ruamel import yaml
import os
import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

def get_cookie(yamlName = "login_cookie.yaml"):
    f = os.path.abspath(os.path.dirname(__file__))
    p = f + '\login_cookie.yaml'
    f = open(p)
    value = f.read()
    cookie_all = yaml.load(value)
    cookie_name = cookie_all['name']
    cookie_value = cookie_all['value']
    cookie_data_dict = {'name':cookie_name,'value':cookie_value}
    print(cookie_data_dict)
    return cookie_data_dict
get_cookie()