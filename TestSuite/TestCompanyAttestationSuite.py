# coding:utf-8
import unittest
from PageObject.PersonalResetPswPageObject import Reset_psw
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText
from PageObject.CompanyAttestationPageObject import Com_Attestation
from public.SQLconnect import MySQLUtil

driverbase = DriverBase()
submit_data = get_excel_data('submit_attestation')
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)
sql_data = get_excel_data('sql_data')

class CompanyAttestation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driverbase.open_broswer()
        driverbase.max_window()
        cls.driver.implicitly_wait(10)
        cls.reset_psw = Reset_psw(cls.driver)
        cls.toast = ToastText(cls.driver)
        cls.atte = Com_Attestation(cls.driver)
    @classmethod
    def tearDownClass(cls):
        driverbase.quit_broswer()
    # 全部为空时，点击提交审核
    def test_all_empty(self):
        mysql.update(sql_data[0]['table'], sql_data[0]['set or search'], sql_data[0]['where'])  # 修改当前公司字段为0
        mysql.update(sql_data[1]['table'], sql_data[1]['set or search'], sql_data[1]['where'])  # 更新 成都知道创宇信息计数有限公司为当前公司
        self.atte.submit_attestation(readconfig.url_admin,submit_data[0]['code'],submit_data[0]['email'],submit_data[0]['path'])
        self.assertEqual(self.atte.com_code_toast(),submit_data[0]['except_result'])
    # 输入错误的企业代码，点击提交审核
    def test_wrror_code(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[1]['code'], submit_data[1]['email'],submit_data[1]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[1]['except_result'])
    # 邮箱为空
    def test_empyt_email(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[2]['code'], submit_data[2]['email'],submit_data[2]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[2]['except_result'])
    # 输入错误的邮箱，点击提交审核
    def test_wrror_email(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[3]['code'], submit_data[3]['email'],submit_data[3]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[3]['except_result'])
    # 未上传营业执照，点击提交审核
    def test_empty_lisence(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[4]['code'], submit_data[4]['email'],submit_data[4]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[4]['except_result'])
    # 上传错误格式的营业执照，点击提交审核
    def test_wrror_lisence(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[5]['code'], submit_data[5]['email'],submit_data[5]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[5]['except_result'])
    # 上传大于5M的营业执照，点击提交审核
    def test_large_lisence(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[6]['code'], submit_data[6]['email'],submit_data[6]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[6]['except_result'])
    # 提交审核成功
    def test_submit_success(self):
        self.atte.submit_attestation(readconfig.url_admin, submit_data[7]['code'], submit_data[7]['email'],submit_data[7]['path'])
        self.assertEqual(self.atte.com_code_toast(), submit_data[7]['except_result'])
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CompanyAttestation('test_all_empty'))
    suite.addTest(CompanyAttestation('test_wrror_code'))
    suite.addTest(CompanyAttestation('test_empyt_email'))
    suite.addTest(CompanyAttestation('test_wrror_email'))
    suite.addTest(CompanyAttestation('test_empty_lisence'))
    suite.addTest(CompanyAttestation('test_wrror_lisence'))
    suite.addTest(CompanyAttestation('test_large_lisence'))
    suite.addTest(CompanyAttestation('test_submit_success'))
    unittest.TextTestRunner().run(suite)