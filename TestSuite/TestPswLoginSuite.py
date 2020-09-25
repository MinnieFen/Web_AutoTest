# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText
import ddt
url = readconfig.url_login
logindata = get_excel_data('psw_login')
driverbase = DriverBase()
@ddt.ddt
class Test_psw_login(unittest.TestCase):
    # def setUp(self):
    #     self.driver = driverBase.open_broswer()
    #     driverBase.max_window()
    #     self.login = Login(self.driver)
    #     self.driver.implicitly_wait(10)
    #     self.toast = ToastText(self.driver)
    # def tearDown(self):
    #     driverBase.quit_broswer()

    # 启动一次浏览器，用例都执行完后，关闭浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = driverbase.open_broswer()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.login = Login(cls.driver)
        cls.toast = ToastText(cls.driver)
    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()

    # def test_login_nullpsw(self):
    #     '''账号正确，密码为空登录'''
    #     self.login.psw_login(logindata[0]['phone'],logindata[0]['psw'],url)
    #     self.assertEqual(self.toast.page_toast(),logindata[0]['except_result'])
    # def test_login_nullphone(self):
    #     '''账号为空，密码正确'''
    #     self.login.psw_login(logindata[1]['phone'],logindata[1]['psw'],url)
    #     self.assertEqual(self.toast.page_toast(),logindata[1]['except_result'])
    # def test_login_allnull(self):
    #     '''账号和密码都为空'''
    #     self.login.psw_login(logindata[2]['phone'],logindata[2]['psw'],url)
    #     self.assertEqual(self.toast.page_toast(),logindata[2]['except_result'])
    # def test_login_mismatch(self):
    #     '''账号和密码不匹配'''
    #     self.login.psw_login(logindata[3]['phone'],logindata[3]['psw'],url)
    #     self.assertEqual(self.toast.sever_toast(),logindata[3]['except_result'])
    # def test_login(self):
    #     '''账号密码正确登录'''
    #     # login = Login(self.driver)
    #     self.login.psw_login(logindata[4]['phone'],logindata[4]['psw'],url)
    #     self.assertEqual(self.login.login_success_username(),logindata[4]['except_result'])
    @ddt.data(*logindata)
    def test_login_ddt(self,data):
        self.login.psw_login(data['phone'],data['psw'],url)
        # self.assertEqual(self.toast.page_toast(),data['except_result'])
        reslut = self.login.is_login_success()
        self.assertTrue(reslut)

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Test_psw_login('test_login'))
    # suite.addTest(Test_psw_login('test_login_nullpsw'))
    # suite.addTest(Test_psw_login('test_login_nullphone'))
    # suite.addTest(Test_psw_login('test_login_allnull'))
    # suite.addTest(Test_psw_login('test_login_mismatch'))
    # unittest.TextTestRunner().run(suite)
