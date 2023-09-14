# @Project ：Python_study 
# @File    ：11.获取当前仓库中所有的key.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:37

from redis import Redis

redis_client = Redis()
res = redis_client.keys()
print(res)