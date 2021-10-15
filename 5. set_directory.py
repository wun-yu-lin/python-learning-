## set
##字典 key-value [key]=value
##in not in
##del 刪除key-value

#set {不出現重複}
#s1 = {2,4,6}
#print (3 in s1)
#print (4 in s1)
#print (4 not in s1)

# set 運算 &=交集  |=聯集  -=差集  ^=反交集(取不重疊部分)
#s1 = {2,4,6,8,10}
#s2 = {4,6,8,9}
#s3 = s1 & s2
#s4 = s1 | s2
#s5 = s1 - s2
#s6 = s2 - s1
#s7 = s1^s2
#print (s3)
#print (s4)
#print (s5)
#print (s6)
#print (s7)

#set (字串) 不出現重複字母
#s1= set ("hello nico")
#print (s1)
#print ( "h" in s1)

#字典的運算 (dic) "key":"value"
#dic1 = {"hello nico":"good band", "winnine":"維尼"}
#dic1["hello nico"] = "best band"
#print(dic1["hello nico"])
#print("test" in dic1)

##刪除字典中的key-value
#print (dic1)
#del dic1["winnine"]   
#print (dic1)

#字典的運算
dic = {x:x*100 for x in [3,4,5]}   #以x從列表[]當中產生字典
print (dic)

dic2 = {y:len(y) for y in ["hello", "nico", "band"]}
print (dic2)
