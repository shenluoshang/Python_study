# @Project ：Python_study 
# @File    ：2.并发任务.py
# @Author  ：魏洪志
# @Date    ：2023/9/12 22:32

import time
import threading


def work_1():
    print('任务1...')
    time.sleep(2)


def work_2():
    print('任务2...')
    time.sleep(2)


t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

t1.start()
t2.start()
