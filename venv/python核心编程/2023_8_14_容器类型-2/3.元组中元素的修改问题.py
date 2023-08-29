# @Project ：Python_study 
# @File    ：3.元组中元素的修改问题.py
# @Author  ：魏洪志
# @Date    ：2023/8/29 23:19

nums = (1, 2, 3)

# 元组不允许修改元素值
# nums[1] = 4

int_list_tuple = (1, [2, 3], 4)

# 在修改元组中的列表的值的时候，有没有修改这个列表在内存中的地址？
int_list_tuple[1][0] = 0
print(int_list_tuple)

"""
如果元组中存在可变类型，则可以修改可变类型中的元素值

    可变类型
        列表
        集合
        字典
        ···
    不可变类型
        整形
        浮点
        元组
        布尔
        字符串
        ···
        
元组是为了保护数据安全的
"""


def get_data():
    return 1, 2, 3

print(get_data())

int_data = (i for i in range(10))   #不是元组推导式，是生成器

obj = iter(int_data)
while True:
    try:
        print(next(obj))
    except StopIteration:
        break