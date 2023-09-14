# @Project ：Python_study 
# @File    ：2.如何使用异常类.py
# @Author  ：魏洪志
# @Date    ：2023/9/5 22:02


# 使用异常捕获防止代码崩溃
try:
    print(a)
except NameError:
    print('当前变量没有定义···')
