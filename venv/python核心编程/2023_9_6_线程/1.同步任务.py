# @Project ：Python_study 
# @File    ：1.同步任务.py
# @Author  ：魏洪志
# @Date    ：2023/9/12 22:28

'''
同步任务：
    必须等待任务1执行完成之后才能执行任务2
'''


import time


def work_1():
    print('任务1...')
    time.sleep(2)


def work_2():
    print('任务2...')
    time.sleep(2)

work_1()
work_2()