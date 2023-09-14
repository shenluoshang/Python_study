# @Project ：Python_study
# @File    ：7.数据添加.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:28

from redis import Redis

redis_client = Redis()

res = redis_client.set('name', '安娜')

print(res)
