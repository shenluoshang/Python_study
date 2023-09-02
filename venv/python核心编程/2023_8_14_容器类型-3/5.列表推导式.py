# @Project ：Python_study 
# @File    ：5.列表推导式.py
# @Author  ：魏洪志
# @Date    ：2023/9/2 21:11


# 生成1 - 20范围内的数字
data_1 = [i for i in range(1, 21)]
print(data_1)

# 生成1 - 20范围内的偶数
data_2 = [i for i in range(1, 21) if i % 2 == 0]
print(data_2)

# 生成列表元组序列
data_3 = [(x, y) for x in range(1, 3) for y in range(3)]
print(data_3)

# 生成列表字典序列
data_3 = [{x: y} for x in range(1, 3) for y in range(3)]
print(data_3)

data_5 = [x for x in range(1, 101)]
data_5 = [data_5[x:x + 3] for x in range(0, len(data_5), 3)]
print(data_5)
