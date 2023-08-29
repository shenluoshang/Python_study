# @Project ：Python_study 
# @File    ：8.列表排序.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 3:57

int_data = [3, 1, 4, 2, 5]
int_data.sort()
print(int_data)

# 从大到小排序
int_data.sort(reverse=True)
print(int_data)

# 上方代码已经翻转过一次，再进行翻转则显示正序
int_data.reverse()
print(int_data)

