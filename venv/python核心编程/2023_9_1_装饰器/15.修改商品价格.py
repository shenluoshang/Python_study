# @Project ：Python_study 
# @File    ：15.修改商品价格.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:39

class Goods:
    def __init__(self):
        self.原价 = 100
        self.折扣 = 0.8

    @property
    def price(self):
        new_price = self.原价 * self.折扣
        return new_price

    @price.setter
    def price(self, value):
        self.原价 = value

    @price.deleter
    def price(self):
        print(1)
        del self.折扣


goods = Goods()
print(goods.price)
goods.原价 = 120
print(goods.price)

del goods.price
