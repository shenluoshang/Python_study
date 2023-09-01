# @Project ：Python_study 
# @File    ：13.实现翻页功能.py
# @Author  ：魏洪志
# @Date    ：2023/9/1 21:19

class Page:
    def __init__(self, page):
        self.page = page
        self.per_num = 10

    @property
    def start(self):
        val = (self.page - 1) * self.per_num
        return val + 1

    @property
    def end(self):
        val = self.page * self.per_num
        return val


page = Page(1)
print(page.start)
print(page.end)
