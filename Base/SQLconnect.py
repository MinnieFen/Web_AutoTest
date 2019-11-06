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
    @staticmethod    # 声明静态方法，调用该函数时不需要实例化
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
            return rows
    def mysql_close(self):
        try:
            # MySQLUtil().connect().close()
            self.conn.close()
        except Exception as a:
            print('关闭数据库异常：%s' %a)
if __name__ == '__main__':
    mysql = MySQLUtil()
    sql = '''SELECT `CODE` from sms_code_record WHERE PHONE = '18782038146' ORDER BY CTIME DESC'''
    mysql.get_execute(sql)
    codes = mysql.get_rows(sql)
    print(codes)
    print(type(codes))
    print(codes[0])
    mysql.mysql_close()
