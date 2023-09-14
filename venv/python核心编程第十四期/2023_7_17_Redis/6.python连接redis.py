# @Project ：Python_study 
# @File    ：6.python连接redis.py
# @Author  ：魏洪志
# @Date    ：2023/9/3 22:23

from redis import Redis

# 1.创建链接
db = Redis()

# 2.打印连接对象，在链接的过程中建议使用异常捕获
print(db)
