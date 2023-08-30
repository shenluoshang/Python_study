# @Project ：Python_study 
# @File    ：2.生成器的工作流程.py
# @Author  ：魏洪志
# @Date    ：2023/8/30 20:11


def my_range(num):
    print('开始迭代...')
    i = 0
    while i < num:
        print('迭代中...')
        '''
        当前生成器是一种状态机，第一次遇到yield则程序暂停
        当第二次运行的时候程序会从之前暂停的地方继续向下执行
        '''
        yield i
        print('-------')
        i += 1
        print('迭代结束')


gen_obj = my_range(3)
print(next(gen_obj))
print(next(gen_obj))


'''

'''