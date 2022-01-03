#字串
s = "Hello nico"
s = "Hello \" nico"  ##\=跳脫 出現"
s = "Hello" "nico" #串接
s= "Hello\nnico" #\n換行
s= "Hello"*3+"nico"  #重複+字
print (s)

#字串編號，第一個字為0開始編號
print(s[6])
print(s[1:5])
print(s[1:])