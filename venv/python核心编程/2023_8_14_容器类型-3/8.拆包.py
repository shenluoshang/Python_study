# @Project ：Python_study 
# @File    ：8.拆包.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 21:24

list_nums = [1, 2, 3, 4]
num_1, num_2, num_3, num_4 = list_nums
print(num_1, num_2, num_3, num_4)

info = {'name': '安娜', 'age': 20}
for key, value in info.items():
    print(key, value)


def get_data(*args, **kwargs):
    print(*args, *kwargs)


get_data(1, 2, 3, 4, name='安娜', age=16)
