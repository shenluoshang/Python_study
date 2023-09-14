# @Project ：Python_study 
# @File    ：8.数据获取.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:32

from redis import Redis

redis_client = Redis()

data = redis_client.get('name')

print(data.decode())
