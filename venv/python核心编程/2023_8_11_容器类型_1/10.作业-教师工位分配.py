# @Project ：Python_study 
# @File    ：10.作业-教师工位分配.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 4:14

'''
一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

'''
import random

# 定义列表用来保存3个办公室
offices = [[], [], []]

# 定义8位老师的名字
teacher_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 进行随机教师分配
for name in teacher_names:
    offices_number = random.randint(0, 2)
    offices[offices_number].append(name)

# 进行结果宣布
i = 1
for offices_number in offices:
    print('第%d个办公室有%d位老师,分别为%s' % (i, len(offices[i - 1]), offices_number))

    i += 1
