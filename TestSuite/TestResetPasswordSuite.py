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
        self.login.send_code_reset(url,logindata[0]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'],sqldata[3]['table'],sqldata[3]['where'])
        self.login.psw_reset(codes[0],logindata[0]['psw'])
        self.assertEqual(self.login.login_error_sever(),logindata[0]['except_result'])
    # 手机号为空
    def reset_empty_phone(self):
        '''请输入手机号'''
        self.login.send_code_reset(url, logindata[1]['phone'])
        self.assertEqual(self.login.login_error_page(),logindata[1]['except_result'])
    # 错误的验证码
    def error_code(self):
        '''验证码错误'''
        self.login.send_code_reset(url, logindata[2]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
        self.login.psw_reset(codes[1], logindata[2]['psw'])
        self.assertEqual(self.login.login_error_sever(), logindata[2]['except_result'])
    # 新密码为全数字
    def error_new_psw(self):
        '''密码错误'''
        self.login.send_code_reset(url, logindata[3]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
        self.login.psw_reset(codes[0], logindata[3]['psw'])
        self.assertEqual(self.login.login_error_sever(), logindata[3]['except_result'])
    # 新密码为全英文
    def new_psw_error(self):
        '''密码错误'''
        self.login.send_code_reset(url, logindata[4]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
        self.login.psw_reset(codes[0], logindata[4]['psw'])
        self.assertEqual(self.login.login_error_sever(), logindata[4]['except_result'])
    # 新密码小于6位
    def less_new_psw(self):
        '''密码错误'''
        self.login.send_code_reset(url, logindata[5]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
        self.login.psw_reset(codes[0], logindata[5]['psw'])
        self.assertEqual(self.login.login_error_sever(), logindata[5]['except_result'])
    # 新密码大于16位
    def more_new_psw(self):
        '''密码错误'''
        self.login.send_code_reset(url, logindata[6]['phone'])
        codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
        self.login.psw_reset(codes[0], logindata[6]['psw'])
        self.assertEqual(self.login.login_error_sever(), logindata[6]['except_result'])
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Reset_password('reset_success'))
    # suite.addTest(Reset_password('reset_empty_phone'))
    suite.addTest(Reset_password('error_code'))
    suite.addTest(Reset_password('error_new_psw'))
    suite.addTest(Reset_password('new_psw_error'))
    suite.addTest(Reset_password('less_new_psw'))
    suite.addTest(Reset_password('more_new_psw'))
    unittest.TextTestRunner().run(suite)