# coding:utf-8
import unittest
from PageObject.HomepagePageObject import HomePage
from public.GetExcelData import get_excel_data
from Base.DriverBase import DriverBase
from config import readconfig
from public.SQLconnect import MySQLUtil

from PageObject.AddCompanyPageObject import Add_company

sqldata = get_excel_data('sql_data')
driverbase = DriverBase()
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)

class Home_Page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driverbase.open_broswer()
        driverbase.max_window()
        cls.driver.implicitly_wait(10)
        cls.home = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()

    def my_all_contract(self):
        self.home.click_homepage_list(readconfig.url_admin)
        all_num_page = self.home.my_contract()
        all_num = list(mysql.select(sqldata[16]['set or search'],sqldata[16]['table'],sqldata[16]['where']))
        print(type(all_num_page))
        print(type(all_num))
        self.assertEqual(all_num_page,' '.join(all_num))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Home_Page('my_all_contract'))
    unittest.TextTestRunner().run(suite)