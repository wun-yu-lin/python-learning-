# #程式碼包奘再一個區塊中，方便隨時呼叫使用 
#函示讓參數有彈性 
# 先定義再呼叫

# 定義函式
# def 函式名稱(參數名稱):
#    函式內部的程式碼

# def sayHello():
#     print ("hello")
# sayHello()

# def say(your_name):
#     print (your_name)
# say(your_name=123)

# def add(n1,n2):    #兩個以上參數用 , 隔開
#     results = n1+n2
#     print(results)
# add(1,2)

# 回傳值
# def 函式名稱 (參數名稱):
#     內部執行碼
#     return #結束函式,回傳 None

# def 函式名稱 (參數名稱):
#     內部執行碼
#     return 資料 #結束函式,回傳資料
##return 能夠幫助資料帶出函式

# #定義函式
# def say (words):
#     return (words,"nico")
# #呼叫函式
# w = say("hello")

# print (w)    ######呼叫函數 取得回傳值########


#函式需要呼叫才會運行


###程式的包裝:同樣的邏輯可以重複利用

def sum (n1,n2):
    sum = 0
    for x in range(n1,n2+1):
        sum+=x
    return sum

sum1 = sum(100,101)
print (sum1)






