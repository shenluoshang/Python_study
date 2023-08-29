# @Project ：Python_study
# @File    ：3.切片.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 0:22

str_data = 'abcdef'

# 结束位置不包含自身
print(str_data[0:4])
print(str_data[:3])

# 取到最后一个字符的前一个字符
print(str_data[:-1])

# 去除所有字符 少见
print(str_data[:])

# 定义起始位置但没有结束位
print(str_data[2:])