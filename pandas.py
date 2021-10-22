# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 02:21:34 2021

@author: wunyu
"""

#pandas 的主要資料結構可以分成Series和DataFrame
# DataFrame的每一列稱為Series，可由多個series組成DF
# Numpy的格式轉成pandas物件格式，用意在於可以使用Numpy不具備的數學函式，資料篩選、群組化等

import pandas as pd

######建立Series物件############

idx = ["a","b","c","d"]
data = [1,2,3,4]
series = pd.Series(data, index=idx)

series.shape  #series 形狀

# 取series當中的元素
fruits = {"a":1,"b":2,"c":3,"d":4}
series2 = pd.Series(fruits)

series2[0:2]
series2[["a","b"]]
series2.index # 取得index
series2.values # 取得values

e_element = pd.Series([5],index=["e"])
series2 = series2.append(e_element) #新增物件
series2 = series2.drop("e")  #刪除物件


#使用條件式從Series篩選想要的元素
conditions = [False,False,True,True]
series2[conditions]

series2[series2>2]  #設定條件篩選
series2[series2>2][series2<4] #設定多條件篩選

#series 排序
series2.sort_index(ascending=True) #使用index 做排序，ascending =True or False 代表正序or倒序
series2.sort_values(ascending=True) #使用value 做排序，ascending =True or False 代表正序or倒序

######建立dataFrame物件#################

#方法1 - 將多個series串接起來，每個series的元素必須相同
df1 = pd.DataFrame([series2,series2,series2])  

#方法2 - 使用key-value建立dataframe
data = {"data":[1,2,3,4,5,6,7],
        "rt":[100,200,300,400,500,600,700],
        "mz":[101,102,103,104,105,106,107]
        }
df2 = pd.DataFrame(data)

      
#方法3 - 傳入數值在定義column name
data = [1,2,3,4,5,6,7]
rt = [100,200,300,400,500,600,700]
mz = [101,102,103,104,105,106,107]
data2 = {"data":data,
         "rt":rt,
         "mz":mz
    }
df3 = pd.DataFrame(data2)
##########

#修改dataFrame的index或column名稱
df1 = pd.DataFrame([series2,series2,series2]) 
df1.index=[1,2,3] #改index
df1.columns= ["a","b","c","d"] #改column name

#df append
## series 物件為按照原先series中index值傳入df中的"特定"index，所以series的index與DF的column name必須一樣!!!!!!
# series欄位不相同時，缺少會出現NaN
df1 = df1.append(series2, ignore_index=True)  

# 新增欄位
df1["e"] = [1,2,3,4]

#建立新的series後，傳入df建立新欄位
new_series = pd.Series([1,2,3,4], index=[0,1,2,3])
df1["new"]=new_series

#取出dataframe中特定元素
# df物件名稱.loc[row列,column行] #依照index的"名稱"索引
data = [1,2,3,4,5,6,7]
rt = [100,200,300,400,500,600,700]
mz = [101,102,103,104,105,106,107]
data2 = {"data":data,
         "rt":rt,
         "mz":mz
    }
idx2 = ["a","b","c","d","e","f","g"]
df3 = pd.DataFrame(data2, index=idx2)
df3.loc[["a","b"],["rt","mz"]] #取出index"名稱為a、b, 且column name為rt、mz的資料


# df物件名稱.loc[row列,column行] #依照index的編號來索引
df3.iloc[[1,2],[0,2]]  #取出index"編號"1、2列row, 0、2列column 

#刪除df的數據
# df物件名稱.drop()
df3.drop(["a","b"], axis=0) #刪除列, 刪除"名稱"為a、b的row列
df3.drop(["mz","rt"], axis=1) #刪除行, 刪除"名稱"為mz、rt的column

#df大小排序
#df物件名稱.sort_values(by="column name", ascending=True)


#df物件中篩選想要的資料
#df物件[row or column的條件式]  #取True 捨棄False
df3[df3.rt > 400]   #rt大於400篩出來


import numpy as np
np.random.seed(0)
columns = ["a","b","c","d","e"]
df4 = pd.DataFrame()
for x in columns:
    df4[x]=np.random.choice(range(100,200),10)
    
df5 =df4    
#print(df4[df4.b >150])
#print(df4[df4.a>150])
#上面是用兩個條件篩選df數據

#print(df5.loc[df5["a"]>100][df5["b"]>100])

##################
#DataFrame串接跟合併 concat() merge
#concat()進行串接 --> DF以"指定方向"串接起來
#merge()()合併 --> 多個DF的某欄位相同，透過該欄位來合併資料
import pandas as pd
#pd.concat([df1,df2],axis=0) #axis來調整串接的方向
dd1 = pd.DataFrame()
dd2 = pd.DataFrame()
np.random.seed(1)

def make_df (index,columns,seed):
    np.random.seed(seed)
    df=pd.DataFrame()
    for x in columns:
        df[x]=np.random.choice(range(1,100),len(index))
    df.index = index
    return df

columns = ["apple","orange","banana"]
df_data1 = make_df(range(10), columns, 1)
df_data2 = make_df(range(10), columns, 0)
print(pd.concat([df_data1,df_data2], axis=0))
print(pd.concat([df_data1,df_data2], axis=1))

#Df merge分成交集合併跟聯集合併
#pd.merge(df左,df右, on =Key欄位, how="inner") #inner交集, outer聯集
#pd.merge(左側df,右側df,left_on="左df欄位",right_on="右側df欄位",how="合併方式") #用index合併就打 right_index=True
dataA = {"id":[1000,1001,1002],"item_id":[2546,4352,342],"customer_id":[103,101,101]}
dataB = {"id":[101,102,103],"name":["Tanaka","Suzuki","Kato"]} 
dfA = pd.DataFrame(data = dataA, index=range(3))
dfB = pd.DataFrame(data = dataB, index=range(3))
dfAB = pd.merge(dfA,dfB,left_on="customer_id",right_on="id",how="inner")



#import file by pandas
#read csv
#df = pd.read_csv("file path")
import pandas as pd
from numpy import nan
df = pd.read_csv("C:/Users/wunyu/Documents/123.csv",header=None) #header為是否第一欄當column name
df.columns=["scan ID","scan type","m/z_start","m/z_end"] #改column name

#另一種方式,使用一行程式來定義
columns=["scan ID","scan type","m/z_start","m/z_end"]
df = pd.read_csv("C:/Users/wunyu/Documents/123.csv",header=None, names=columns)

#write csv (存檔)
#df.to_csv("file path")
df.to_csv("C:/Users/wunyu/Documents/456.csv")

#去除NaN值
#dropna，去除含有Nan的row
df.iloc[1,2]= nan
df.dropna()  #去除NaN,None,##Listwise
df[[0,1,2]].dropna() #針對0-2 column來去除Nan值


##填補NaN值ㄝ
#df物件名稱.fillna(填補值)
import pandas as pd
from numpy import nan
df = pd.read_csv("C:/Users/wunyu/Documents/123.csv")
df.iloc[0:6,2:4]=nan
df=df.fillna(0)

#使用前一列的資料來填補
df = pd.read_csv("C:/Users/wunyu/Documents/123.csv")
df.iloc[5:6,2:4]=nan
df=df.fillna(method="ffill")

#判斷重複資料 duplicated(),drop_duplicated()
#df物件.duplicated() #return True or False series物件
#df物件.drop_duplicates() #return 刪除重複數據後的資料
 

#使用map來利用df的原有column生成新column
#新series欄位物件 = 舊 series 欄位物件.map(對照表)  #對照表通常使用dict字典
df1 = pd.read_csv("C:/Users/wunyu/Documents/locatiion.csv")
city_map = {"AA":"AAA","BB":"BBB","CC":"CCC","DD":"DDD","EE":"EEE","FF":"FFF"}
df1["region"]=df1["city"].map(city_map)


##劃分、篩選df資料 #cut #只能數字
#pd.cut(指定Series欄位物件, 區間數量或自定義的區間list)
df1_cut = pd.cut(df1["ID"],3) #column "ID"切成三等份

df1_cut_counts = pd.value_counts(df1_cut)

#如何定義劃分範圍及範圍區間名稱
ID_bins = [99,103,105]   #定義劃分範圍
ID_labels = ["ID in 100-103", "ID in 104-105"] # #定義範圍名稱
df1_cut_labels = pd.cut(df1["ID"],ID_bins,labels=ID_labels) #劃分
pd.value_counts(df1_cut_labels) #計算區間的數據數量
df1["ID range"] = df1_cut_labels  #區間資料傳入DataFrame



#取得頭尾列row
#head() 取得前幾筆數據
#tail() 取得最後幾筆數據


#_______________________________________________________


#df進行四則運算
import pandas as pd
import numpy as np
np.random.seed(0)
columns = ["A","B","C","D","E"]
df111 = pd.DataFrame()

for x in columns:
    df111[x]=np.random.choice(range(10,20),10)
    
duble_df111 = df111*2
square_df111 = df111**2
sqrrt_df = np.sqrt(df111)

#快速取得統計數據 df.describe()
df111_des = df111.describe()
df111_des.loc["mean"] #抓取mean數據

#計算row or column之間的差 diff
df111.diff(-2,axis=0) #表示下兩列的差距

#分組統計 df.groupby("欄位")
group_data = {"Prefecture":["Tokyo","Kanagawa","Osaka","Kyoto","Aichi"],"Area":[2190,2415,1904,4610,5172],"Population":[13636,9145,8837,2605,7505],"Region":["Kanto","Kanto","Kinki","Kinki","Chubu"]}
group_df = pd.DataFrame(group_data)
group_region =group_df.groupby("Region")
mean_df = group_region.mean()
