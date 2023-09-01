# @Project ：Python_study 
# @File    ：12.获取商品的价格.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:18


class Shop:

    @property
    def money(self):
        return 100


shop = Shop()
print(shop.money)
