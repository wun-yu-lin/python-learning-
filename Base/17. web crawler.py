##web crawler 網路爬蟲基本篇

#基本流程  1.連線到特定網址，抓取資料 2.解析資料，取得實際想要的部分
#關鍵心法  盡可能讓程式模仿一個普通試用者的樣子
#解析資料 json 使用內建模組即可
#HHTML 格式資料   第三方套件 BeautifulSoup
#安裝套件 PIP 套件管理工具  安裝 BeautifulSoup

import urllib.request as request
www = "https://www.ptt.cc/bbs/Olympics_ISG/index.html"
web = request.Request(www, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
})
with request.urlopen(web) as webdata:
    data = webdata.read().decode(encoding="utf-8")
#解析資料
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles =root.find_all("div",class_="title") #尋找 class="title" 的 div 標籤
for title in titles:
    if title.a!= None:
        print(title.a.string)