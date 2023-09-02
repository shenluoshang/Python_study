# @Project ：Python_study 
# @File    ：2.创建表.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 0:15

import pymysql


def create_table():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='201314',db='python_test_1')

    cursor = db.cursor()

    sql = '''
        create table employee(
            first_name varchar(20) not null,
            last_name varchar (20),
            age int,
            sex varchar(1),
            income float ,
            create_time datetime
            );    
    '''

    # 使用异常处理执行sql
    try:
        cursor.execute(sql)
        # cursor.execute('select version()')
        # res = cursor.fetchone()
        # print(res)

        print('创建成功！')

    except Exception as ex:
        print(f'创建失败~原因为：{ex}')
    finally:
        db.close()

create_table()
