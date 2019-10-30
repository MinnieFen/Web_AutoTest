# coding:utf-8
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from config import readconfig
from common.operate_page import BasePage

class Login(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Firefox()
        url = readconfig.url
        self.d.get(url)
    def tearDown(self):
        userName = self.d.find_element(By.XPATH, '//*[@class = "dropdown-toggle"]').text
        self.assertEqual(userName, u'晨曦')
        self.d.quit()
    def test_login1(self):
        inputPhone = readconfig.inputPhone
        inputPsw = readconfig.inputPsw
        B = BasePage(self.d)
        B.find_web_element(By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a').click()
        B.find_web_element(By.XPATH,'//*[@id="login_span_type_pwd"]').click()
        B.find_web_element(By.XPATH,'// *[@id = "login_id_input_phone"]').send_keys(inputPhone)
        B.find_web_element(By.XPATH,'//*[@id ="login_id_input_password"]').send_keys(inputPsw)
        B.find_web_element(By.XPATH,'//*[@id="login_id_login"]').click()
        sleep(3)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login('test_login1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)