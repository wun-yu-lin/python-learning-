# # def 函式名稱 (參數名稱 = 預設資料):
# #   函式內部的程式碼
# def say (msg ="hello nico"):
#     print (msg)
# say ()

# def power(base=10,exp=0):
#     print(base**exp)
# power (exp=10,base = 100)


# #名稱對應
# def 函式名稱 (n1,n2):
#     函式內部程式碼
# #呼叫函式，以參數名稱對應資料
# 函式名稱 (n2= 1,n1 =3)   #參數順序沒有差別


#無限長度參數
# def 函式名稱 (*無限參數):
#     無限參數以Tuple 資料型態處理
#     函式內部程式碼
# 函式名稱 (參數1,參數2,參數3)
def avg(*num1):
    sum = 0
    for x in num1:
        sum+=x
    avg1 = sum/len(num1)
    return (avg1)

y = avg (1,2,3,4,5,6,7,8,9)
print (y)