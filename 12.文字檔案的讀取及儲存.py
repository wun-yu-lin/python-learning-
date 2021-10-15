##讀取、儲存文字檔案
##開啟檔案>讀取或寫入>關閉檔案

##開啟檔案
# 檔案物件 = open(檔案路徑,mode=開啟模式)
# 開啟模式: 讀取=r 寫入 = w 讀寫 = r+
# 讀取全部文字 檔案物件.read()
# 一次讀取一行 
# for 變數 in 檔案物件:
#   從檔案依序讀取每行文字到變數中
# #寫入文字
# 檔案物件.write(字串)
# #寫入換行符號
# 檔案物件.write("範例\n")

# #讀取json格式
# import json
# 讀取到的資料 = json.load(檔案物件)
# json.dump(要寫入的資料,檔案物件)
# 檔案物件.close()    #每次開啟檔案都要將檔案關閉 這是必須的

# #最佳實務  以下區塊會自動、安全的關閉檔案 不需要close
# with open(檔案路徑, mode=開啟模式) as 檔案物件:
#     讀取或寫入檔案的程式

#寫入檔案
# file = open("data.txt",mode ="w")
# file.write("Hello nico\ngoodband")
# file.close()

# #寫入檔案_中文     encoding = "UTF-8","UTF-16", "Big5"
# file = open("data_tai.txt",mode ="w", encoding="utf-8")
# file.write("Hello nico\n是個好樂團")
# file.close()

#最佳實務
# with open("data_best.txt",mode = "w",encoding="utf-8") as file:
#     file.write("Hello nico\n是個好樂團")

# #檔案讀取
# with open("data_best.txt",mode="r",encoding="utf-8") as file123:
#     data = file123.read()
# print(data)

#讀取數字並且將每一行的數字加起來
# sum=0
# with open("data_num.txt",mode="r") as file_num:
#     for x in file_num:
#         sum+=int(x)
# print (sum)

# 使用 JSON　格式讀取、複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data 是一個字典
print ("naem:",data["name"])
print ("version:",data["version"])

data["name"]="New name"
with open ("config.json", mode="w") as file:
    json.dump(data, file)