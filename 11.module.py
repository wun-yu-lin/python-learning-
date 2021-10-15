##模組  獨立的程式檔案 可被其他程式使用 獨立的程式檔案
#載入 > 使用  先載入模組，再使用模組中的函式或變數
# import 模組名稱 (檔案名稱)
# import 模組名稱 as 模組別名
#模組名稱或別名.函式名稱(參數資料)
#模組名稱或別名.變數名稱

#內建模組
#sys 模組 系統相關的資訊

# #載入模組
# import sys 
# #使用sys模組
# print(sys.platform) #作業系統
# print(sys.path) #搜尋模組的路徑

# #載入模組
# import sys as s   #(s=別名)
# #使用sys模組
# print(s.platform) #作業系統
# print(s.path) #搜尋模組的路徑 模組必續放在這些路徑當中

#自訂模組
#建立幾何運算模組
#建立檔案 genometry.py 定義平面幾何運算的函式
#載入與使用 
import sys
sys.path.append("C:\python test\modules")   #在模組搜尋路徑列表中 [新稱路徑]
print(sys.path) #搜尋模組的路徑 模組必續放在這些路徑當中
import geometry
dis = geometry.distance(x1=1,x2=2,y1=1,y2=2)
print (dis)
slo = geometry.slope(x1=1,x2=2,y1=1,y2=2)
print (slo)

