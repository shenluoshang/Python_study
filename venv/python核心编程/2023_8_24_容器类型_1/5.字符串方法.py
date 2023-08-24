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

print(str_data_2.startswith('a'))
print(str_data_2.endswith('f'))

# 在web开发中如果需要完成验证码验证，需要忽略用户的大小写
print(str_data_2.lower())
print(str_data_2.upper())

str_data_3 = ' 你 好 '
print(str_data_3)
print(str_data_3.strip())

str_data_4 = '1234a'
print(str_data_4.isdigit())

str_data_5 = ['你好','双双','请你吃猪蹄']
my_str = ' '
print(my_str.join(str_data_5))

