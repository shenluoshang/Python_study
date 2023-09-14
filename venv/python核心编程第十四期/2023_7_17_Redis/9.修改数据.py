# @Project ：Python_study 
# @File    ：9.修改数据.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:34

from redis import Redis

redis_client = Redis()

redis_client.set('name', '双双')
res = redis_client.get('name')
print(res.decode())
