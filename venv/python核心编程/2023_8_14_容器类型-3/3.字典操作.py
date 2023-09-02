# @Project ：Python_study 
# @File    ：3.字典操作.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 20:37

stu_info = {
    'name': '双双',
    'age': 18,
    'address': '南京',

}

'''
数据获取
'''
print(stu_info['name'])
print(stu_info.get('name'))

# 当前直接写入key，如果key不存在则报错
# print(stu_info['tel'])

# 使用get获取不存在的key不会报错，默认返回None，返回值可以自定义
print(stu_info.get('tel', '当前电话不存在'))

'''
数据修改
'''

stu_info['address'] = '北京'
print(stu_info)

'''
数据插入
'''
stu_info['gender'] = '女'
print(stu_info)

'''
数据删除
'''
# 删除指定的key,不会将整个字典删除
del stu_info['name']

# 清空字典
stu_info.clear()
print(stu_info)

# 直接删除字典数据结构
del stu_info

# 空字典的声明
new_dict_1 = {}
new_dict_2 = dict()
print(new_dict_1, new_dict_2)

# 字典转换
teacher_dict_info = {
    'name': '何老师',
    'age': 18,
    'gender': '男',

}

result = teacher_dict_info.items()
print(list(result))
