# coding:utf-8
import unittest
from PageObject.PersonalResetPswPageObject import Reset_psw
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText
from PageObject.LoginPageObject import Login
from PageObject.AddCompanyPageObject import Add_company

resetdata = get_excel_data('personal_resetpsw')
sqldata = get_excel_data('sql_data')
driverbase = DriverBase()

class Personal_resetpsw(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driverbase.open_broswer()
        driverbase.max_window()
        cls.driver.implicitly_wait(10)
        cls.reset_psw = Reset_psw(cls.driver)
        cls.toast = ToastText(cls.driver)
        cls.login = Login(cls.driver)
        cls.add = Add_company(cls.driver)
    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()

    # 验证码和密码都为空时，点击确定修改按钮
    def test_all_empty(self):
        '''个人中心修改密码模块，使用账号：18782038104 的账号来进行测试'''
        # self.reset_psw.reset_psw_empty(readconfig.url_admin)
        self.login.psw_login(readconfig.inputPhone_reset,readconfig.inputPsw_reset,readconfig.url_login)   # 调用登录模块进行密码登录，登录一次后，后面的用例都不需要再次登录
        self.add.first_login()     # 进入个人中心页面
        self.reset_psw.reset_psw_empty()
        self.assertEqual(self.reset_psw.code_toast(),resetdata[0]['except_result'])

    # 输入验证码，不输入新密码
    def test_psw_empty(self):
        self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0],resetdata[1]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[1]['except_result'])

    # 输入密码小于5位数字
    def test_less_psw(self):
        # self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0],resetdata[2]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[2]['except_result'])

    # 输入密码超过16位数字
    def test_more_psw(self):
        # self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0],resetdata[3]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[3]['except_result'])

    # 6位全数字密码
    def test_all_num_psw(self):
        # self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0], resetdata[4]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(), resetdata[4]['except_result'])

    # 6位全英文密码
    def test_all_letter_psw(self):
        # self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0], resetdata[5]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(), resetdata[5]['except_result'])

    # 输入全为空格的密码
    def test_all_blank(self):
        # self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0], resetdata[6]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(), resetdata[6]['except_result'])

    # 输入错误的验证码
    def test_error_code(self):
        # self.reset_psw.click_code(readconfig.url_admin)
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0], resetdata[7]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(), resetdata[7]['except_result'])

    # 修改密码成功，a1234567
    def test_right_psw(self):
        self.reset_psw.click_code()
        # self.reset_psw.click_code(readconfig.url_admin)
        codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0], resetdata[8]['new_password'])
        self.assertEqual(self.reset_psw.get_reset_text(), resetdata[8]['except_result'])

    # 修改密码成功后，重新登录
    def test_reset_login(self):
        self.login.psw_login(readconfig.inputPhone_reset,resetdata[8]['new_password'],readconfig.url_login)
        self.assertEqual(self.login.login_success_username(),resetdata[9]['except_result'])
        self.login.logout()

    # 重置密码为原密码，a123456，方便后续使用
    def test_reset_befor(self):
        self.login.psw_login(readconfig.inputPhone_reset,resetdata[8]['new_password'],readconfig.url_login)   # 调用密码登录模块
        self.add.first_login()    # 进入个人中心页面
        self.reset_psw.click_code()
        codes = self.reset_psw.get_code(sqldata[15]['set or search'], sqldata[15]['table'], sqldata[15]['where'])
        self.reset_psw.reset_psw(codes[0],readconfig.inputPsw_reset)
        self.assertEqual(self.reset_psw.get_reset_text(), resetdata[8]['except_result'])

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Personal_resetpsw('test_all_empty'))
    # suite.addTest(Personal_resetpsw('test_psw_empty'))
    # suite.addTest(Personal_resetpsw('test_less_psw'))
    # suite.addTest(Personal_resetpsw('test_more_psw'))
    # suite.addTest(Personal_resetpsw('test_all_num_psw'))
    # suite.addTest(Personal_resetpsw('test_all_letter_psw'))
    suite.addTest(Personal_resetpsw('test_all_blank'))
    # suite.addTest(Personal_resetpsw('test_error_code'))
    # suite.addTest(Personal_resetpsw('test_right_psw'))
    # suite.addTest(Personal_resetpsw('test_reset_login'))
    # suite.addTest(Personal_resetpsw('test_reset_befor'))
    unittest.TextTestRunner().run(suite)