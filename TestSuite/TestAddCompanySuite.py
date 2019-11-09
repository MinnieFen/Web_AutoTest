# coding:utf-8
from PageObject.AddCompanyPageObject import Add_company
from Base.DriverBase import DriverBase
import unittest
from config import readconfig
driverbase = DriverBase()
class AddCompany(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        driverbase.max_window()
    def tearDown(self):
        driverbase.quit_broswer()
    # 添加公司成功
    def test_addCompany_01(self):
        add = Add_company(self.driver)
        add.add_company(readconfig.inputPhone_cookie,readconfig.inputPsw_cookie,readconfig.url_login,'金控集团4',readconfig.url_admin)
        self.assertEqual(add.companyName(),'金控集团4')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AddCompany('test_addCompany_01'))
    # suite.addTest(AddCompany('test_login_02'))
    # suite.addTest(AddCompany('test_login_03'))
    # suite.addTest(AddCompany('test_login_04'))
    # suite.addTest(AddCompany('test_login_05'))
    unittest.TextTestRunner().run(suite)