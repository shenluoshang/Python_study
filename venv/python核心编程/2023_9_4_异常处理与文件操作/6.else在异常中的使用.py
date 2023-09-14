# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:37
# @Author  : 顾安
# @File    : 6.else在异常中的使用.py
# @Software: PyCharm


try:
    print('测试代码...')
    # 手动抛出异常
    # raise StopIteration
    # 根据条件是否成立决定异常是否抛出
    # assert 条件, 异常类型/自定义信息
except:  # 不需要判断, 因为会检测所有的异常类的基类
    print('程序异常...')
else:
    print('如果程序没有出现任何异常的情况下, 则执行当前语句...')
