# @Project ：Python_study 
# @File    ：5.创建带有参数的内部函数闭包.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:27

def add(num_1):
    def add_wrappear(num_2):
        print('两数之和：', num_1 + num_2)

    return add_wrappear


func_obj = add(5)
func_obj(3)
