# @Project ：Python_study 
# @File    ：5.迭代器.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 20:39

'''
可迭代对象：
    告诉for循环当前对象是可以被执行的对象

迭代器：
    实现重复取值的方法实现
'''

from collections.abc import Iterable,Iterator

# 是否是一个可迭代对象
int_list=[1,2,3]


# 可迭代对象不一定就是迭代器对象
# print(isinstance(int_list,Iterable))
# print(isinstance(int_list,Iterator))

# 通过python内置的Iter方法让可迭代对象生成迭代器
iter_obj = iter(int_list)
# print(iter_obj)
# print(isinstance(iter_obj,Iterator))

'''
python内置的iter方法可以返回一个可迭代对象的迭代器
    不一定能正确返回
'''

# 迭代器有什么用？
'''
迭代器可以被for循环执行并且也可以被next方法执行
    迭代器取值的方向一定是从左往右的
'''
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
# print(next(iter_obj)) # 越界报错



