# @Project ：Python_study 
# @File    ：6.线程方法.py
# @Author  ：魏洪志
# @Date    ：2023/9/20 21:19


'''
start方法
join方法
daemon方法： 守护线程
    默认情况下主线程需要等待子线程所有任务运行完毕之后主线程才会退出
        但是如果子线程遇到的是死循环任务，主线程就无法退出
    使用守护线程的方法：主线程运行完毕之后直接退出，不等待子线程
        主线程一旦退出，那么所有的子线程全部死亡
'''
import threading
import time

num = 0


def add():
    global num
    for i in range(100000000):
        # time.sleep(0.1)
        num += 1


# 线程对象
t = threading.Thread(target=add)
# 使用start开起一个线程并运行
t.start()
# t.join()  # 让主线程指定到join之后阻塞主线程，直到子线程任务完成
print(num)
