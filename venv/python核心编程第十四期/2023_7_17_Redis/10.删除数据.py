# @Project ：Python_study 
# @File    ：10.删除数据.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:35

from redis import Redis

redis_client = Redis()
res = redis_client.delete('name')
print(res)