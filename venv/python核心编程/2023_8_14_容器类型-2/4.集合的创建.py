# @Project ：Python_study 
# @File    ：4.集合的创建.py
# @Author  ：魏洪志
# @Date    ：2023/8/29 23:37

'''
集合：
    集合数据类型与列表类型类似
        集合数据类型是无序的
        集合数据类型可以进行数据去重
'''

set_data = {1, 2, 3, 4}
print(type(set_data))
print(set_data)

for item in set_data:
    print(item)

# 集合不能使用元素下表取值
# print(set_data[0])

# 创建空集合
set_data_1 = {} # 不能使用当前形式去创建空集合，当前语句创建的对象为字典
set_data_2 = set()

print(type(set_data_1), type(set_data_2))
