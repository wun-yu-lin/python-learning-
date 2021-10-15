##網路連線、公開資料串連
##下載特定網址資料
from os import read
import urllib.request as request
# src="https://www.nchu.edu.tw"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") ##取得網址的數據
#     print(data)


import json
kkk="https://datacenter.taichung.gov.tw/swagger/OpenData/418f82cc-19c1-459e-9205-a272d4af289e"
with request.urlopen(kkk) as webdata:
    wdata=json.load(webdata)
    # print(wdata)

for station in wdata:
    print(wdata["坐標E"])