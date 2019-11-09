# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login
from Base.GetExcelData import get_excel_data
# from Base.MyUnit import MyTest
from config import readconfig
from Base.DriverBase import DriverBase

url = readconfig.url_login
logindata = get_excel_data('logindata')
driverBase = DriverBase()
class Test_login(unittest.TestCase):
    def setUp(self):
        self.driver = driverBase.open_broswer()
        driverBase.max_window()
    def tearDown(self):
        driverBase.quit_broswer()
    def test_login_01(self):
        '''账号密码正确登录'''
        login = Login(self.driver)
        login.psw_login(logindata[0]['phone'],logindata[0]['psw'],url)
        self.assertEqual(login.login_success_username(),logindata[0]['except_result'])
    def test_login_02(self):
        '''账号正确，密码为空登录'''
        login = Login(self.driver)
        login.psw_login(logindata[1]['phone'],logindata[1]['psw'],url)
        self.assertEqual(login.login_error_page(),logindata[1]['except_result'])
    def test_login_03(self):
        '''账号为空，密码正确'''
        login = Login(self.driver)
        login.psw_login(logindata[2]['phone'],logindata[2]['psw'],url)
        self.assertEqual(login.login_error_page(),logindata[2]['except_result'])
    def test_login_04(self):
        '''账号和密码都为空'''
        login = Login(self.driver)
        login.psw_login(logindata[3]['phone'],logindata[3]['psw'],url)
        self.assertEqual(login.login_error_page(),logindata[3]['except_result'])
    def test_login_05(self):
        '''账号和密码不匹配'''
        login = Login(self.driver)
        login.psw_login(logindata[4]['phone'],logindata[4]['psw'],url)
        self.assertEqual(login.login_error_sever(),logindata[4]['except_result'])
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_login('test_login_01'))
    # suite.addTest(Test_login('test_login_02'))
    # suite.addTest(Test_login('test_login_03'))
    # suite.addTest(Test_login('test_login_04'))
    # suite.addTest(Test_login('test_login_05'))
    unittest.TextTestRunner().run(suite)
