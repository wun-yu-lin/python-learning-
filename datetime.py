##datetime 模組-儲存加減 時間資料

import datetime as dt
datetime = dt.datetime(year=2021, month=8, day = 30)
print(datetime)
timedelta = dt.timedelta(days = 100, seconds = 1000)
print(timedelta)
y = datetime
z = timedelta
print (y-z)
print (y-z*100)
x = dt.datetime(2021,8,21,17,0,0)
s1 =x.strftime("%Y %m %d %H %M %S")  ##按照格式輸入
s2 =x.strftime("%Y年 %m月 %d日 %H時 %M分 %S秒")



        
import pandas as pd
time = pd.DataFrame([[2021,8,21],[2020,8,21],[1000,8,21]])

for x in range(3):
    for Y, M, D in [list(time.iloc[x])]:
        print(Y,M,D)
        
        
str1 = "2021/8/30"
datetime1 = dt.datetime.strptime(str1,"%Y/%m/%d")