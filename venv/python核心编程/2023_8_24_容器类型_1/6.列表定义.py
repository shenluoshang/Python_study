# @Project ：Python_study 
# @File    ：6.列表定义.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 2:55

'''
列表：
    Python中的一种数据结构，可以用于存储不同类型的对象
'''

students_names = ['顾安', '安娜', '双双', '夏洛']

# 打印列表
print(students_names)

# 索引取值
print(students_names[2])

# 切片取值
print(students_names[1:])

# 列表倒序
print(students_names[::-1])

# 对于容器类型的迭代取值
str_data = 'abcdefg'

# for i in str_data:
#     print(i)
#
#
# for i in students_names:
#     print(i)

# 使用while循环获取容器类型中的元素
list_lenth = len(students_names)
i = 0
while i < list_lenth:
    print(students_names[i])
    i += 1

# 列表可以存储任意类型数据
data_info = ['安娜', 18, 178, 64, True]

# 列表声明的两种方式

# 1.通过字面量进行声明
list_data_1 = []
list_data_2 = list()
print(list_data_1,list_data_2)
