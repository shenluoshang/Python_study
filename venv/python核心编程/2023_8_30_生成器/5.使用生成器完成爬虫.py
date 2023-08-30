# @Project ：Python_study 
# @File    ：5.使用生成器完成爬虫.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 20:49

import requests

url = 'https://www.baidu.com?page_id={}'

def get_data(url):
    for i in range(30):
        response = requests.get(url).content
        yield response

# for item in get_data(url):
#     print(item)


import asyncio
