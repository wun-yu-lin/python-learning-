# ##內建模組
# ##學習random & statistics 模組 

# #亂數模組
import random
# n1 = random.choice([0,1,5,8])   #隨機選1個資料
# n2 = random.sample([0,2,5,8,9,5,4,6,8,9,8],5)  #隨機取樣n個資料
# print (n1)
# print (n2)
# data = [0,2,3,5,8]
# random.shuffle(data)
# print(data)

# random.random()   #0~1.0 之間取隨機亂數
# n3 = random.uniform(0.0, 1.0)  
# print(n3)

# n4 = random.normalvariate(100,10)   #取平均數100且標準差為10的常態分布亂數
# print (n4)


# ##載入統計模組
# import statistics 
# statistics.mean()平均值
# statistics.median()中位數
# statistics.stdev()標準差

# import random
# import statistics
# n5 = random.seed(0)
# # statistics.mean()
# print(n5)


# data = random.uniform(100,1000)  #隨機亂數
# print(data)

# #常態分配 100 標準差20 數據在100+-20之間
# data = random.normalvariate(100,20)
# print(data)
