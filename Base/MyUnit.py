# coding:utf-8
# from Base.DriverBase import start_driver
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = start_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()