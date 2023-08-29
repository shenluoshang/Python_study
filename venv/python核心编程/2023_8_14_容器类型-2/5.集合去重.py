# @Project ：Python_study 
# @File    ：5.集合去重.py
# @Author  ：魏洪志
# @Date    ：2023/8/29 23:56

int_set_data = {1, 1, 2, 2, 3, 4, 5, 2}
print(int_set_data)

stu_info = {'安娜','双双','安娜','夏洛'}

new_stu_info = set(stu_info)
print(list(new_stu_info))