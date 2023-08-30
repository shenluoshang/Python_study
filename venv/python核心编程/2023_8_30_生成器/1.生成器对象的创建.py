# @Project ：Python_study 
# @File    ：1.生成器对象的创建.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 20:08

# 生成器可以使用函数进行创建
def my_range(nums):
    i = 0
    while i < nums:
        yield i #如果函数中出现了yield，则当前函数为一个生成器
        i += 1



# 生成器对象是一种特殊的迭代器，使用for循环去运行生成器
gen_obj = my_range(5)
# for i in gen_pbj:
#     print(i)


print(next(gen_obj))