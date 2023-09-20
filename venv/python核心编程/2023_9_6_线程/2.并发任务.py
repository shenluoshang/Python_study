# @Project ：Python_study 
# @File    ：2.并发任务.py
# @Author  ：魏洪志
# @Date    ：2023/9/12 22:32

import time
import threading


def work_1():
    for i in range(5):
        print('任务1...')
        time.sleep(2)


def work_2():
    for i in range(5):
        print('任务2...')
        time.sleep(2)


t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

t1.start()
t2.start()


'''
子线程1 和子线程2 是谁创建的
    子线程1和子线程2是主线程创建的 那么当前主线程在运行的第一行代码的时候当前两个子线程存不存在？
    
    主线程不能被切换，主线程在运行代码的时候是单线程同步代码
        t1先被启动，则子线程1先运行
        t2后运行
        
        仅限于启动的时候
        
    
'''