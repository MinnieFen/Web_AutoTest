# coding:utf-8
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect(host = 'rm-2ze034s22kk79pys5o.mysql.rds.aliyuncs.com',user = 'cdtest',port=3336,password = 'uIkKCZgNay',db = 'yxtestdev4',charset = 'utf8')
cursor = db.cursor()    # 使用cursor方法获取操作游标
# sql语句
sql = '''select'''
cursor.execute(sql)      # 执行SQL
db.commit()     # 提交到数据库执行
# result = cursor.fetchall()    # 获取所有的结果
# result = cursor.fetchone()    # 获取一条结果
result = cursor.fetchmany(2)    # 获取前两条数据
print(result)
db.close()    # 关闭数据库连接