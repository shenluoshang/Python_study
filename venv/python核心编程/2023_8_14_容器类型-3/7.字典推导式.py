# @Project ：Python_study 
# @File    ：7.字典推导式.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 21:21

# 获取1 - 10 范围内key值为当前元素，value是当前元素的平方
dict_data = {x: x ** 2 for x in range(1, 11)}
print(dict_data)
