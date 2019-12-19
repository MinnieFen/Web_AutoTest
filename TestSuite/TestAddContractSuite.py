# conding:utf-8
from Base.DriverBase import DriverBase
from PageObject.AddContractPageObject import Add_Contract
from Base.GetExcelData import get_excel_data
from config import readconfig
from Base.SQLconnect import MySQLUtil
import unittest

driverbase = DriverBase()
contract_data = get_excel_data('add_contract')
sql_data = get_excel_data('sql_data')
class AddContract(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.add = Add_Contract(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 添加已完成契约
    def test_add_contract_01(self):
        mysql = MySQLUtil(db= readconfig.sql_db_qiyuebao)
        mysql.update(sql_data[0]['table'],sql_data[0]['set or search'],sql_data[0]['where'])
        mysql.update(sql_data[1]['table'],sql_data[1]['set or search'],sql_data[1]['where'])
        count  = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])    # 统计添加契约前，改公司的总契约数
        self.add.add_finish_contract(contract_data[0]['company_name'],contract_data[0]['describe'],contract_data[0]['appraise'],readconfig.url_admin)
        count_new = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])
        mysql.mysql_close()
        self.assertEqual(int(count_new[0][0]),int(count[0][0])+1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AddContract('test_add_contract_01'))
    unittest.TextTestRunner().run(suite)