# @Project ：Python_study 
# @File    ：3.生成器表达式.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 20:19


# 列表推导式
int_list = [i for i in range(1, 6)]

print(int_list)

# 生成器表达式
gen_obj = (i for i in range(1, 6) if i % 2 == 0)
print(gen_obj)

'''
生成器是一种特殊的迭代器
    __iter__
    __next__
'''

print('__iter__' in dir(gen_obj))
print('__next__' in dir(gen_obj))

gen = (i for i in range(10000) if i % 2 == 0)
# 通过求和函数获取生成器中所有元素的和
print(sum(gen))
# print(next(gen))
