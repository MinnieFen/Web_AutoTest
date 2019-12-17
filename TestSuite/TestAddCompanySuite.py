# coding:utf-8
from PageObject.AddCompanyPageObject import Add_company
from Base.DriverBase import DriverBase
import unittest
from config import readconfig
from Base.GetExcelData import get_excel_data
driverbase = DriverBase()
companyName = get_excel_data('company_name')
class AddCompany(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        driverbase.max_window()
        self.driver.implicitly_wait(10)
        self.add = Add_company(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 公司名为空
    def test_addCompany_01(self):
        # add = Add_company(self.driver)
        self.add.save_login_cookie(readconfig.inputPhone_cookie,readconfig.inputPsw_cookie,readconfig.url_login)    # 登录一次，后面的不用再次登录
        # add.add_company(readconfig.inputPhone_cookie,readconfig.inputPsw_cookie,readconfig.url_login,companyName[0]['name'],readconfig.url_admin)
        self.add.add_company(companyName[0]['name'],readconfig.url_admin)
        self.assertEqual(self.add.add_error_page(),companyName[0]['except_result'])
    # 添加公司，默认行业
    def test_addCompany_02(self):
        # add = Add_company(self.driver)
        self.add.add_company(companyName[1]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[1]['except_result'])
    # 添加公司，选择教育培训行业
    def test_addCompany_03(self):
        # add = Add_company(self.driver)
        self.add.add_company_education(companyName[2]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[2]['except_result'])
    #添加公司，选择水利水电行业
    def test_addCompany_04(self):
        self.add.add_company_waterboard(companyName[3]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[3]['except_result'])
    #添加已存在的公司
    def test_addCompany_05(self):
        self.add.add_company_education(companyName[4]['name'],readconfig.url_admin)
        self.assertEqual(self.add.add_error_sever(),companyName[4]['except_result'])
    # 添加已被认证的公司
    def test_addCompany_06(self):
        self.add.add_company_education(companyName[5]['name'],readconfig.url_admin)
        self.assertEqual(self.add.add_error_sever(),companyName[5]['except_result'])
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(AddCompany('test_addCompany_01'))
    # suite.addTest(AddCompany('test_addCompany_02'))
    # suite.addTest(AddCompany('test_addCompany_03'))
    # suite.addTest(AddCompany('test_addCompany_04'))
    # suite.addTest(AddCompany('test_addCompany_05'))
    # unittest.TextTestRunner().run(suite)