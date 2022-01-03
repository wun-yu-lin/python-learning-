##注意!相當複雜!!
# 1. 類別與類別屬性
# 2. 類別與實體物件、實體屬性
# 先定義類別，再透過類別建立實體物件
# 建立>使用
# 先建立實體物件，然後才能使用實體屬性

#建立實體
# class 類別名稱:
#     定義初始化函式
#     def__init__(self):
#         透過操作 self 來定義實體屬性
# #建立實體物件，放入變數obj中
# obj=類別名稱() #呼叫初始化函式

# class Point:
#     def __init__ (self):
#         self.x=3
#         self.y=4
# #建立實體物件
# #此實體物件包含X和Y兩個實體屬性


# p = Point()


# class Point:
#     def __init__ (self,x,y):
#         self.x=x
#         self.y=y
# p = Point(1,5)

# #使用實體物件     實體物件.實體屬性的名稱
# print(p.x,p.y)
# #建立第二個實體物件
# p2 = Point(2,3)
# print(p2.x,p2.y)

#Fullname 實體物件的設計: 分開紀錄性、名資料的全名
# class Fullname:
#     def __init__(self,frist,last):
#         self.frist = frist
#         self.last = last
# name1 = Fullname(frist="lin", last="wunyu")
# print(name1.frist,name1.last)
#實體屬性，封裝在實體物件中的變數
#實體方法 封裝在實體物件中的韓式

# class 類別名稱:
#     #定義初始化函式
#     def __init__(self):
#         定義實體屬性
#     定義實體方法/函式
#     def 方法名稱(self, 更多自訂參數):
#         方法主體, 透過 self 操作實體物件
# #建立實體物件，放入變數obj中
# obj = 類別名稱()

class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def distance (self, targetX, targetY):
        return ((((self.x-targetX)**2)+((self.y-targetY)**2)))**0.5
p=Point(3,4)
p.show()
dis1 = p.distance(0,0) ##計算座標3,4與座標0,0的距離
print(dis1)

class File:
    def __init__(self, name):
        self.name=name
        self.file=None
    def open1 (self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read1 (self):
        return self.file.read()
f1 = File ("data.txt")
f1.open1()
data = f1.read1()
print(data)