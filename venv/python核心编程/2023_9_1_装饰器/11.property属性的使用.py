# @Project ：Python_study 
# @File    ：11.property属性的使用.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:13


class Foo:
    num = 0

    @property
    def get_num(self):
        return self.num


print(Foo.num)
foo = Foo()
res = foo.get_num
print(res)
