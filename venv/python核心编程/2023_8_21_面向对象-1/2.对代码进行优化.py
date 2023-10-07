# @Project ：Python_study 
# @File    ：2.对代码进行优化.py
# @Author  ：魏洪志
# @Date    ：2023/10/7 21:39

names = ['双双', '安娜', '夏洛']
ages = [18, 16, 60]


def print_student_info(name, age):
    print(f'姓名:{name},年龄:{age}')


for name, age in zip(names, ages):
    print(name, age)
