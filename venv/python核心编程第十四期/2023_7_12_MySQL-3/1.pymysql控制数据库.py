# @Project ：Python_study 
# @File    ：1.pymysql控制数据库.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 23:48

# 使用Python完成数据的增删改查
# 借助Python的mysql驱动进行连接， pymysql

import pymysql


def db_connect():
    # 1.连接数据库
    db = pymysql.connect(host='localhost', user='root', password='201314', db='python_test_1', port=3306)

    # 2.当前连接对象中存在游标方法
    cursor = db.cursor()

    # 3.游标对象可以执行sql指令
    cursor.execute('select * from students')

    # 4.获取结果
    sql_data = cursor.fetchall()

    # 5.打印结果
    print(sql_data)

    # 6.关闭连接
    db.close()


db_connect()
