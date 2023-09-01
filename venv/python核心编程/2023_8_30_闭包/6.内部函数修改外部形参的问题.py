# @Project ：Python_study 
# @File    ：6.内部函数修改外部形参的问题.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:28

def counter(number=0):
    def add_wrapper():
        # 如果当前内部函数需要修改外部函数的变量 需要添加一个关键字
        '''
        global: 全局变量
        nonlocal: 函数之间
        :return:
        '''
        nonlocal number
        number += 1
        print(number)

    return add_wrapper


func_obj = counter(3)
func_obj()
