# @Project ：Python_study 
# @File    ：8.__call__方法.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 20:48

class My_wrapper:
    def __call__(self, *args, **kwargs):
        print('我被调用了...')


my_wrapper = My_wrapper()
my_wrapper()