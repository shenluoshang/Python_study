# @Project ：Python_study 
# @File    ：5.字符串方法.py
# @Author  ：魏洪志
# @Date    ：2023/8/25 0:47

str_data_1 = 'abcdef'

print(str_data_1.find('c'))

print(str_data_1.count('a'))

print(str_data_1.replace('a','A',1))

str_data_2 = 'a,b,c,d,e,f'
print(str_data_2.split(','))
res = str_data_2.split(',')
print(res)