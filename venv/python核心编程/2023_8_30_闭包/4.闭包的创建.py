# @Project ：Python_study 
# @File    ：4.闭包的创建.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 21:20

def make_printer(message):
    def printer():
        print(message)

    return printer


func_obj = make_printer('你好')
func_obj()
