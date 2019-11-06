# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login

class Test_login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_login_01(self):
        Login().psw_login()
