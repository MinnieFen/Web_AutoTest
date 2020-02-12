# coding:utf-8
from Base.DriverBase import DriverBase
from PageObject.AddContractPageObject import Add_Contract
from Base.GetExcelData import get_excel_data
from config import readconfig
from Base.SQLconnect import MySQLUtil
import unittest

driverbase = DriverBase()
contract_list_data = get_excel_data('contract_list')
sql_data = get_excel_data('sql_data')
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)

class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.add = Add_Contract(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 待我确认列表，确认契约
    def test_confirm_contract(self):
        mysql.update(sql_data[0]['table'], sql_data[0]['set or search'], sql_data[0]['where'])  # 修改当前公司字段为0
        mysql.update(sql_data[1]['table'], sql_data[1]['set or search'], sql_data[1]['where'])  # 更新 成都知道创宇信息计数有限公司为当前公司
        num_wait_confirm_1 = self.add.wait_confirm_num()
        num_wait_complete_1 = self.add.wait_complete_num()
        self.add.confirm_ensure(readconfig.url_admin)
        num_wait_confirm_2 = self.add.wait_confirm_num()
        num_wait_complete_2 = self.add.wait_complete_num()
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2+1)
        self.assertEqual(num_wait_complete_1,num_wait_complete_2-1)
    # 待我确认列表取消确认契约
    def test_cancel_confirm_contract(self):
        num_wait_confirm_1 = self.add.wait_confirm_num()
        self.add.confirm_cancel(readconfig.url_admin)
        num_wait_confirm_2 = self.add.wait_confirm_num()
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2)
    # 待我确认列表，确定拒绝契约
    def test_refuse_contract(self):
        num_wait_confirm_1 = self.add.wait_confirm_num()
        self.add.refuse_ensure(readconfig.url_admin,contract_list_data[0]['reason'])
        num_wait_confirm_2 = self.add.wait_confirm_num()
        self.assertEqual(self.add.add_error_sever(),contract_list_data[0]['except_result'])
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2+1)
    # 待我确认列表，确定拒绝契约，内容为空
    def test_refuse_contract_empty(self):
        self.add.refuse_ensure(readconfig.url_admin, contract_list_data[1]['reason'])
        self.assertEqual(self.add.add_error_page(), contract_list_data[1]['except_result'])
    # 待我确认列表，取消拒绝契约
    def test_cancel_refuse_contract(self):
        num_wait_confirm_1 = self.add.wait_confirm_num()
        self.add.refuse_cancel(readconfig.url_admin,contract_list_data[2]['reason'])
        num_wait_confirm_2 = self.add.wait_confirm_num()
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2)
    # 待我完成列表，取消确认完成
    def test_cancel_complete(self):
        num_wait_complete_1 = self.add.wait_complete_num()
        self.add.complete_cancel(readconfig.url_admin)
        num_wait_complete_2 = self.add.wait_complete_num()
        self.assertEqual(num_wait_complete_1,num_wait_complete_2)
    # 待我完成列表，确认完成
    def test_complete_contract(self):
        num_wait_complete_1 = self.add.wait_complete_num()
        self.add.confirm_ensure(readconfig.url_admin)
        num_wait_complete_2 = self.add.wait_complete_num()
        self.assertEqual(num_wait_complete_1,num_wait_complete_2+1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ContractList('test_confirm_contract'))
    # suite.addTest(ContractList('test_cancel_confirm_contract'))
    unittest.TextTestRunner().run(suite)