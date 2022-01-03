#break #強制結束迴圈，一定要寫在迴圈內
# n=0
# while n < 5:
#     if n == 3:
#         break
#     n+=2
# print (n)

# #continue  #迴圈強制進入下一圈

# n = 0
# for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
#     if x%2==0:
#         continue
#     n+=1
# print (n)


# #else 迴圈結束前 先執行再跳出迴圈

# x = 0 
# while x <10:
#     x+=1
# else:
#     print (x)

# sum = 0
# for x in range(11):
#     sum+=x
# else:
#     print (sum)

#綜合範例: 找出整數的平方根
print ("此程式可以判斷整數有沒有正整平方根")
x = input ("請輸入一個整數:")
x = int (x)
for i in range(x):
    if i*i == x:
        print (i,"為正整數解")  
        break
else:
    print ("無正整數平方根")
