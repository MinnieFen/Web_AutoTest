# coding:utf-8
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from config import readconfig

cur_path = os.path.dirname(os.path.realpath(__file__))
def add_case(caseName = 'PageObject',rule = 'test*.py'):
    case_path = os.path.join(cur_path,caseName)
    discover = unittest.defaultTestLoader()