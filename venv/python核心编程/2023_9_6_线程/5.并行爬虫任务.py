# @Project ：Python_study 
# @File    ：5.并行爬虫任务.py
# @Author  ：魏洪志
# @Date    ：2023/9/19 21:50


import time
import requests
import multiprocessing
import threading


def get_image(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        time.sleep(1)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/98/10792.jpg',
    'http://pic.bizhi360.com/bbpic/98/10386.jpg'
]

if __name__ == '__main__':
    start = time.time()
    for img_url in url_list:
        p = multiprocessing.Process(target=get_image, args=(img_url,))
        p.start()
    end = time.time()
    print('耗时：', end - start)

'''
通过多进程的方式运行代码
    并行运行
    
    
并行与并发的区别
    线程多任务是并发运行的
        在所有任务中，同一时刻只有一个任务被执行，任务可以被切换
    进程多任务是并行运行的
        利用当前CPU的核心执行任务并同时执行
'''
