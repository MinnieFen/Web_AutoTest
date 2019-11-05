# coding:utf-8
import MySQLdb
from config import readconfig
# 打开数据库连接
# db = MySQLdb.connect(host = 'rm-2ze034s22kk79pys5o.mysql.rds.aliyuncs.com',user = 'cdtest',port=3336,password = 'uIkKCZgNay',db = 'yxtestdev4',charset = 'utf8')
# cursor = db.cursor()    # 使用cursor方法获取操作游标
# sql语句
# sql = '''select'''
# cursor.execute(sql)      # 执行SQL
# db.commit()     # 提交到数据库执行
# result = cursor.fetchall()    # 获取所有的结果
# result = cursor.fetchone()    # 获取一条结果
# result = cursor.fetchmany(2)    # 获取前两条数据
# print(result)
# db.close()    # 关闭数据库连接

# sql_info = {'host':'rm-2ze034s22kk79pys5o.mysql.rds.aliyuncs.com',
#             'user':'cdtest',
#             'port':3336,
#             'password':'uIkKCZgNay',
#             'db':'yxtestdev4',
#             'charset':'utf8'}
sql_info = {'host':readconfig.sql_host,
            'user':readconfig.sql_uer,
            'port':readconfig.sql_port,
            'password':readconfig.sql_password,
            'db':readconfig.sql_db_yx,
            'charset':readconfig.sql_charset}
class MySQLUtil():
    def __init__(self):
        self.db_info = sql_info
        self.db = MySQLUtil.__getconnect(self.db_info)
    @staticmethod
    def __getconnect(db_info):
        try:
            db = MySQLdb.connect(host = db_info['host'],
                                 user = db_info['user'],
                                 port = int(db_info['port']),
                                 password = db_info['password'],
                                 db = db_info['db'],
                                 charset = db_info['charset'])
            return db
        except Exception as a:
            print('数据库连接异常：%s' %a)
    def get_execute(self,sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            self.db.rollback()
            print('执行SQL异常：%s' %a)
        else:
            cursor.close()
            self.db.commit()
    def get_rows(self,sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            print('执行SQL异常:%s' %a)
        else:
            self.db.commit()
            rows = cursor.fetchall()
            cursor.close()
            print(rows)
            return rows
    def mysql_close(self):
        try:
            self.db.close()
        except Exception as a:
            print('关闭数据库异常：%s' %a)
if __name__ == '__main__':
    mysql = MySQLUtil()
    sql = '''SELECT 
o.UUID_REQ_OBJECT,o.OBJ_USE_MODE,o.OBJ_NAME,o.MY_COM_NAME,o.CONTRACT_NAME,o.USED_COUNT,o.OBJ_USE_STATUS,o.PARTY_TYPE,o.VERIFY_COUNT
FROM sta_req_object AS o
WHERE o.OBJ_NAME LIKE '%湖南公司'
AND o.OBJ_USE_STATUS = 3
ORDER BY o.CTIME'''
    mysql.get_execute(sql)
    mysql.get_rows(sql)
    mysql.mysql_close()