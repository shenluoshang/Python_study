# @Project ：Python_study 
# @File    ：7.列表方法.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 3:04

# append：在列表中增加元素,添加的元素在列表的最后一位
student_names = ['安娜']
student_names.append('双双')
print(id(student_names))

student_name_1 = ['安娜']
student_name_2 = ['双双']
res = student_name_1 + student_name_2
print(id(res), id(student_name_1), id(student_name_2))

# += 是在原有列表中进行修改，但是如果使用加法则创建一个新列表
student_name = ['安娜']
student_name += ['双双']
print(student_name)

# extend：extend可以写入多个值
new_students = ['佳佳', '何老师', '扶苏']  # 是一个可以被迭代的容器
student_name.extend(new_students)
print(student_name)

# insert:在指定位置插入数据
int_data = [1, 2, 4]

# a = [1, 2]
# b = [3, 4]
# c = list()
# c.append(a) # append 可以将一个列表作为一个最基本的元素添加到列表中
# c.append(b)
# print(c)

int_data.insert(2, 3)
print(int_data)

# 修改
new_students[1] = '木木'
print(new_students)

# 元素查询
name = '安娜'
print(name in student_name)

print(student_name.count(name))

int_data = [1, 1, 2, 3, 4]
print(int_data.count(5))

# 列表元素删除
movie_names = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
# del
del movie_names[0]
print(movie_names)

# pop：弹出
movie = movie_names.pop() # 默认弹出最后一个元素，可以写入弹出的指定元素下标
print(movie_names)
print(movie)

# remove:移除
movie_names.remove('第一滴血')
print(movie_names)
