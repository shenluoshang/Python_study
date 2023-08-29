# @Project ：Python_study 
# @File    ：6.迭代器的本质.py
# @Author  ：魏洪志
# @Date    ：2023/8/28 20:54

int_list = [1, 2, 3, 4, 5]

# for i in int_list:
#     print(i)

# i = 0
# while i < len(int_list):
#     print(int_list[i])
#     i += 1

# 生成一个迭代器
obj_iter = iter(int_list)
while True:
    try:
        print(next(obj_iter))
    except StopIteration:
        break

