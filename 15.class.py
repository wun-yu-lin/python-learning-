##類別
##封裝變數或函式- 封裝的變數或函式，通稱類別的屬性
##Class
# ##定義類別，之後才能使用類別中的屬性   定義>使用
# class 類別名稱:
#     定義封裝的變數
#     定義封裝的函式

# #基本語法
#定義test 類別
# # 類別名稱.屬性名稱
# class Test:
#     x=3 #定義變數
#     def say(): #定義函式
#         print("hello_yo")
# #使用test類別
# Test.x+3 #取得屬性X的資料3
# Test.say() #呼叫屬性say函式 

class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Supported","Read from", src)

#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("interent")

class say_my_name:
    saywhat = ["絕命毒師經典台詞"]
    def say_again(say_again):
        print(say_again, "say_my__name")
print(say_my_name.saywhat)
say_my_name.say_again(say_again="經典台詞")
