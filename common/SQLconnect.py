# coding:utf-8
import MySQLdb
from config import readconfig

class MySQLUtil():
    def __init__(self):
        self.sql_info = {'host': readconfig.sql_host,
                    'user': readconfig.sql_uer,
                    'port': readconfig.sql_port,
                    'password': readconfig.sql_password,
                    'db': readconfig.sql_db_qiyuebao,
                    'charset': readconfig.sql_charset}
        # self.host = readconfig.sql_host
        # self.user = readconfig.sql_uer
        # self.port = readconfig.sql_port
        # self.password = readconfig.sql_password
        # self.dbb = readconfig.sql_db_yx
        # self.charset = readconfig.sql_charset
        self.conn = MySQLUtil.__connect(self.sql_info)
    @staticmethod
    def __connect(sql_info):
        try:
            # conn = MySQLdb.connect(host = self.host,
            #                        user = self.user,
            #                        port = int(self.port),
            #                        password = self.password,
            #                        db = self.dbb,
            #                        charset = self.charset)
            conn = MySQLdb.connect(host = sql_info['host'],
                                   user = sql_info['user'],
                                   port = int(sql_info['port']),
                                   password = sql_info['password'],
                                   db = sql_info['db'],
                                   charset = sql_info['charset'])
            return conn
        except Exception as a:
            print('数据库连接异常：%s' %a)
    def get_execute(self,sql):
        # cursor = MySQLUtil().connect().cursor()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            # MySQLUtil().connect().rollback()
            self.conn.rollback()
            print('执行SQL异常：%s' %a)
        else:
            cursor.close()
            # MySQLUtil().connect().commit()
            self.conn.commit()
    def get_rows(self,sql):
        # cursor = MySQLUtil().connect().cursor()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            print('执行SQL异常:%s' %a)
        else:
            # MySQLUtil().connect().commit()
            self.conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            print(rows)
            return rows
    def mysql_close(self):
        try:
            # MySQLUtil().connect().close()
            self.conn.close()
        except Exception as a:
            print('关闭数据库异常：%s' %a)
# if __name__ == '__main__':
#     mysql = MySQLUtil()
#     sql = '''SELECT
# o.UUID_REQ_OBJECT,o.OBJ_USE_MODE,o.OBJ_NAME,o.MY_COM_NAME,o.CONTRACT_NAME,o.USED_COUNT,o.OBJ_USE_STATUS,o.PARTY_TYPE,o.VERIFY_COUNT
# FROM sta_req_object AS o
# WHERE o.OBJ_NAME LIKE '%湖南公司'
# AND o.OBJ_USE_STATUS = 3
# ORDER BY o.CTIME'''
#     mysql.connect()
#     mysql.get_execute(sql)
#     mysql.get_rows(sql)
#     mysql.mysql_close()
