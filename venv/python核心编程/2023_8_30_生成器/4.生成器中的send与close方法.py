# @Project ：Python_study 
# @File    ：4.生成器中的send与close方法.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 20:29

def my_range(num):
    print('迭代开始...')
    i = 0
    while i < num:
        print('迭代中...')
        value = yield i
        if value == '这是一个被发送出去的值...':
            print(1 + 1)
        i += 1
        print('迭代结束...')


my_range = my_range(5)

print(next(my_range))

# 在第二次执行时换成send进行驱动   send可以用来发送数据：信号
print(my_range.send('这是一个被发送出去的值...'))

'''
使用send的注意点
    1.第一次执行不能使用send发送信号
'''

# close 主要用于关闭生成器对象
my_range.close()
print(my_range)

'''
生成器可以用于爬虫函数
    1.生成器是一种懒加载的机制
        直接去调用生成器函数是不会执行的，返回一个生成器对象，而不是像列表一样直接生成具体的值
        当你第一次调用的时候生成一个值，可以有利于内存优化
        [i for i in range(10000000)]    生成一亿个数据
        
        (i for i in range(10000000)]    只会生成一个数据 ——>生成器对象
        
    2.生成器执行一次只会生成一个值，第二次生成的值会覆盖第一次生成的值
        保证了内存中只有一个值
'''
