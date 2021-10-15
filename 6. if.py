#流程控制 判斷式 (縮排很重要Tab)
#if 布林值一:
    #若布林一值為TRUE,執行命令
#elif 布林值二:
    #若布林值二為TRUE,執行命令
#else:
    #若布林值一跟二為False, 執行命令

#x=input("請輸入數字:") #基本輸入為字串型態
#x=int(x) #轉成整數
#if x >201:
#    print ("他大於200")
#elif x > 101:
#    print ("他介於100到200之間")
#else:
#    print ("他小於100")

#if elif else 跑完任何一段就跳出 所以需要整個結構(三段)去看


#if True:
#    print ("True run")
#else:
#    print ("False no run")
 
# #if False:
#    print ("True run")
#else:
#    print ("False no run")

n1 = input("請給數字A")
n2 = input("請給數字B")
n1 = int (n1)
n2 = int (n2)
cal = input("請輸入怎麼算:加,減,乘,除")

if cal == "加":
    print (n1+n2)
elif cal == "減":
    print (n1-n2)
elif cal == "乘":
    print (n1*n2)
elif cal == "除":
    print (n1/n2)
else:
    print ("錯誤")


