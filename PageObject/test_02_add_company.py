# coding:utf-8
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from Base.login_cookie import Login
from Base import get_yamldata
from config import readconfig
from Base.operate_page import BasePage
from Base import get_exceldata
from time import sleep
from Base.SQLconnect import MySQLUtil
class Add_company(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = webdriver.Firefox()
    def setUp(self):
        # self.d = webdriver.Firefox()
        # Login().test_login()
        # Login().save_cookie()
        cookie_value = get_yamldata.get_cookie()
        url = readconfig.url_admin
        self.d.get(url)
        self.d.add_cookie(cookie_value)
        self.d.get(url)
        self.B = BasePage(self.d)
        add_data = get_exceldata.get_excel_data('addcompany')
        self.data1 = add_data[0]['elements']
        self.data2 = add_data[1]['elements']
        self.data3 = add_data[2]['elements']
        self.data4 = add_data[3]['elements']
        self.data5 = add_data[4]['elements']
        self.data6 = add_data[5]['elements']
        self.data7 = add_data[6]['elements']

    @classmethod
    def tearDownClass(cls):
        mysql = MySQLUtil()
        sql = '''DELETE
        FROM com_user_relation
        WHERE NAME = "金控集团"'''
        mysql.get_execute(sql)
        mysql.mysql_close()
        cls.d.quit()
# 添加不存在的公司
    def test_01_add_company(self):
        companyName = "金控集团"
        # self.B.click_btn(By.XPATH,self.data6)
        # self.B.click_btn(By.XPATH,self.data7)
        self.B.click_btn(By.XPATH,self.data1)
        self.B.click_btn(By.XPATH,self.data2)
        self.B.send_word(companyName,By.XPATH,self.data3)
        self.B.click_btn(By.XPATH,self.data4)
        sleep(3)
        company_now = self.B.get_text(By.XPATH,self.data1)
        self.assertEqual(company_now,companyName)
    def test_02_add_company(self):
        companyName = "金控集团"
        self.B.click_btn(By.XPATH, self.data1)
        self.B.click_btn(By.XPATH, self.data2)
        self.B.send_word(companyName, By.XPATH, self.data3)
        self.B.click_btn(By.XPATH, self.data4)
        result = self.B.get_text(By.XPATH,self.data5)
        self.assertEqual(result,'添加公司已经存在')
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Add_company('test_01_add_company'))
    # TestSuite.addTest(Add_company('test_02_add_company'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
