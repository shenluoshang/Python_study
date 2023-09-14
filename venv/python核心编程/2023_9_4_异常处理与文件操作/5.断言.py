# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 下午8:28
# @Author  : 顾安
# @File    : 5.断言.py
# @Software: PyCharm

"""
断言一般也会用在爬虫程序上
"""

# 断言关键字
# assert 20 < 10, '程序错误'


import requests


response = requests.get('http://www.baidu.com')
assert response.status_code == 200, StopIteration


