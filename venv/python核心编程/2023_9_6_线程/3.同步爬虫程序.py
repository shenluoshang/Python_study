# @Project ：Python_study 
# @File    ：3.同步爬虫程序.py
# @Author  ：魏洪志
# @Date    ：2023/9/19 21:23

import requests
import time

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

start = time.time()
for im_url in url_list:
    get_image(im_url)
end = time.time()
print('耗时:' ,end - start)
