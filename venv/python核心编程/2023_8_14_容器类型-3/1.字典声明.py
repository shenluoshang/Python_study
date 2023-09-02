# @Project ：Python_study 
# @File    ：1.字典声明.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 20:28

'''
字典是puthon中相对重要的一种数据类型
    形式为键值对
'''

stu_info = {
    'name': '安娜',
    'age': 18,
    'address': '长沙',

}

# 第一种for循环运行只能获取到字典中的key
for item in stu_info:
    print(item)

# 第二种for循环只能获取到字典中的value
for item in stu_info.values():
    print(item)

# 元组拆包
for key,value in stu_info.items():
    print(f'{key}--{value}')