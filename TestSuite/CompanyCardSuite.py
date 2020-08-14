# coding:utf-8
import unittest
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText
from PageObject.CompanyCardPageObject import Company_Card

driverbase = DriverBase()
card_data = get_excel_data('company_card')
class CompanyCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driverbase.open_broswer()
        driverbase.max_window()
        cls.driver.implicitly_wait(10)
        cls.toast = ToastText(cls.driver)
        cls.card = Company_Card(cls.driver)
    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()
    # 全部为空时提交数据
    def test_all_empty(self):
        self.card.submit_card(readconfig.url_admin,card_data[0]['logo_path'],card_data[0]['person'],card_data[0]['phone'],card_data[0]['address'],card_data[0]['website'],card_data[0]['introduction'])
        self.assertEqual(self.toast.page_toast(),card_data[0]['except_result'])
    # 必填项输入全空格
    def test_blank(self):
        self.card.submit_card(readconfig.url_admin,card_data[1]['logo_path'],card_data[1]['person'],card_data[1]['phone'],card_data[1]['address'],card_data[1]['website'],card_data[1]['introduction'])
        self.assertEqual(self.toast.page_toast(),card_data[1]['except_result'])
    # 必填项联系电话为空
    def test_empty_phone(self):
        self.card.submit_card(readconfig.url_admin,card_data[2]['logo_path'],card_data[2]['person'],card_data[2]['phone'],card_data[2]['address'],card_data[2]['website'],card_data[2]['introduction'])
        self.assertEqual(self.toast.page_toast(),card_data[2]['except_result'])
    # 必填项联系电话输入非数字
    def test_error_type_phone(self):
        self.card.submit_card(readconfig.url_admin, card_data[3]['logo_path'], card_data[3]['person'],
                              card_data[3]['phone'], card_data[3]['address'], card_data[3]['website'],
                              card_data[3]['introduction'])
        self.assertEqual(self.toast.page_toast(), card_data[3]['except_result'])
    # 只填写联系人和联系电话
    def test_submit(self):
        self.card.submit_card(readconfig.url_admin, card_data[4]['logo_path'], card_data[4]['person'],card_data[4]['phone'], card_data[4]['address'], card_data[4]['website'],card_data[4]['introduction'])
        self.assertEqual(self.toast.page_toast(), card_data[4]['except_result'])
    # 输入所有字段
    def test_all_submit(self):
        self.card.submit_card(readconfig.url_admin, card_data[5]['logo_path'], card_data[5]['person'],
                              card_data[5]['phone'], card_data[5]['address'], card_data[5]['website'],
                              card_data[5]['introduction'])
        self.assertEqual(self.toast.page_toast(), card_data[5]['except_result'])
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(CompanyCard('test_all_empty'))
    # suite.addTest(CompanyCard('test_blank'))
    # suite.addTest(CompanyCard('test_empty_phone'))
    # suite.addTest(CompanyCard('test_error_type_phone'))
    suite.addTest(CompanyCard('test_submit'))
    # suite.addTest(CompanyCard('test_all_submit'))
    unittest.TextTestRunner().run(suite)