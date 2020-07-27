# coding:utf-8
import unittest
from PageObject.PersonalResetPswPageObject import Reset_psw
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText

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
        cls.codes = cls.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()

    # 验证码和密码都为空时，点击确定修改按钮
    def test_all_empty(self):
        self.reset_psw.reset_psw_empty(readconfig.url_admin)
        print(self.reset_psw.code_toast())
        self.assertEqual(self.reset_psw.code_toast(),resetdata[0]['except_result'])

    # 输入验证码，不输入新密码
    def test_psw_empty(self):
        self.reset_psw.click_code(readconfig.url_admin)
        # codes = self.reset_psw.get_code(sqldata[15]['set or search'],sqldata[15]['table'],sqldata[15]['where'])
        self.reset_psw.reset_psw(self.codes[0],resetdata[1]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[1]['except_result'])

    # 输入密码小于5位数字
    def test_less_psw(self):
        self.reset_psw.click_code(readconfig.url_admin)
        self.reset_psw.reset_psw(self.codes[0],resetdata[2]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[2]['except_result'])

    # 输入密码超过16位数字
    def test_more_psw(self):
        self.reset_psw.click_code(readconfig.url_admin)
        self.reset_psw.reset_psw(self.codes[0],resetdata[3]['new_password'])
        self.assertEqual(self.reset_psw.psw_toast(),resetdata[3]['except_result'])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Personal_resetpsw('test_all_empty'))
    # suite.addTest(Personal_resetpsw('test_psw_empty'))
    suite.addTest(Personal_resetpsw('test_less_psw'))
    suite.addTest(Personal_resetpsw('test_more_psw'))
    unittest.TextTestRunner().run(suite)