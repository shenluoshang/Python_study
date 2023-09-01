# @Project ：Python_study 
# @File    ：14.使用property修改数据.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:36

class Goods:
    @property
    def price(self):
        print(1)

    @price.setter
    def price(self,value):
        print(2)

    @price.deleter
    def price(self):
        print(3)

obj = Goods()
print(obj.price)
obj.price = 2