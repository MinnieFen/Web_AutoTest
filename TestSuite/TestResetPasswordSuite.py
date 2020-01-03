# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login
from Base.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase

url = readconfig.url_login
logindata = get_excel_data('logindata')
sqldata = get_excel_data('sql_data')
driverBase = DriverBase()

class Reset_password(unittest.TestCase):
    def setUp(self):
        self.driver = driverBase.open_broswer()
        driverBase.max_window()
        self.login = Login(self.driver)
        self.driver.implicitly_wait(30)
    def tearDown(self):
        driverBase.quit_broswer()
    # 修改密码成功
    def reset_success(self):
        '''密码修改成功'''
        self.login.psw_reset(url,logindata[6]['phone'],logindata[6]['psw'],sqldata[3]['set or search'],sqldata[3]['table'],sqldata[3]['where'])
        self.assertEqual(self.login.login_error_sever(),logindata[6]['except_result'])
    # 手机号为空
    def reset_empty_phone(self):
        '''请输入手机号'''
        self.login.psw_reset(url)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Reset_password('reset_success'))
    unittest.TextTestRunner().run(suite)