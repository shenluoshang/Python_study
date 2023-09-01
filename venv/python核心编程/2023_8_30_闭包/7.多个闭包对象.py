# @Project ：Python_study 
# @File    ：7.多个闭包对象.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:33

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


func_obj_1 = counter()
func_obj_2 = counter()

print(id(func_obj_1), id(func_obj_2))
# func_obj()

'''
func_obj_1和func_obj_2同时指向了一个函数
    当前指向的同一个函数的内存地址是一样的么？
    
在获取内部函数的应用的过程中调用了外层函数，当前外层函数调用了2次，内层函数的地址会被重新生成

当前案例表明了两个变量所接受的函数地址是不一样的，所以当先两个函数是相互独立的，不会互相产生影响
'''
