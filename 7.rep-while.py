#流程控制 迴圈
# while 布林值:  
#    若布林值為True 執行命令
#   回到上方，做下一次的迴圈判斷直到布林值為 False 

#n=2
#while n<10000:
#    print ("變數n的資料是:",n)
#    n**=2


##累加程式 等差及數
#n = 0
#sum = 0
#while n<=100:
#    sum+=n
#    n+=10
#print (sum)



##for 變數名稱 in 列表或字串:
#    將列表中的項目或字串中的字元逐一取出, 逐一處理

#for x in [1,2,3,4,5]:
#   print ("數據的所有字元",x)

#y = input ("請給我一排字，我可以把字拆開:")
#for x in y:
#    print (x)


#for c in "hello":
#    print(c)

#for x in range(15,20):     #range (1,10)  不包含10 只有1~9 range(10)
#    print(x)

#1~1000 相乘起來
#sum = 1
#for x in range (1,1000):
#    sum = sum*x
#print (sum)  


## 給兩串數字 逐一配對
#a = input ("給一串數字:")
#b = input ("給一串字:")
#c = 0
#for x in a:
#    y = b[c]
#    d= {x:y}
#    c+=1
#    print (d)


print ("以下英文及數字數目要相同")
a = input ("給我一串英文:")
b = input ("給我一串數字:")
c = 0
for x in b:
    y = a[c]
    x = int(x)
    c+=1
    d = {x:y}
    print (d)
print ("你一共給",c,"個數字")

x=1
y=2

while x < 10000:
    results = x+y
    x+=1
    y**2
    sum=sum+results
    print (results)
print ("累計",sum)
x= 1
y= 2




