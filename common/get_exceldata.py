# coding:utf-8
from common.read_excel import ReadExcel
import os

# 调用read_excel方法，直接返回数据列表
def get_excel_data(sheetname):
    filepath_now = os.path.abspath(os.path.join(os.getcwd()))
    excel_path = filepath_now + '\data\elementData.xlsx'
    # print(ReadExcel(excel_path,sheetname).read_excel_data())
    return ReadExcel(excel_path,sheetname).read_excel_data()
# get_excel_data('loginpage')