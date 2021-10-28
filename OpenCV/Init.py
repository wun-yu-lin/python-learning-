# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:10:17 2021

@author: wunyu
"""

#色彩三元素 B,G,R #注意順序
import cv2 #載入OpenCV module
import numpy as np
import matplotlib.pyplot as plt


# 調整openCV參數、顏色順序，加入matplotlab繪圖功能
def aidemy_imshow(name,img):
    b,g,r=cv2.split(img)
    img=cv2.merge([r,g,b])
    plt.title(name)
    plt.imshow(img)
    plt.show()
    
cv2.imshow=aidemy_imshow

#OpenCV圖檔方式
#圖片物件名稱 = cv2.imread("路徑/sample.jpg") ,圖片內容直接轉成array格式
#cv2.imshow("title",圖片物件名稱)
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
cv2.imshow("winnie",img)
cv2.imwrite("winnin.jpg",img)

# =============================================================================
# 
# =============================================================================

#建立算數的相片
img=np.random.randint(100,150,size=(256,256,3))
cv2.imshow("random",img)

# =============================================================================
# 
# =============================================================================

#建立B=200,G=100,R=200的圖片,使用蜂巢狀的list來生成100X100的圖片
img=np.array([[(200,100,200) for x in range(100)] for x in range(100)])  
cv2.imshow("B=200,G=100,R=200,100X100 pixel",img)

# =============================================================================
# 
# =============================================================================

#建立漸層圖片
img=np.array([[(x,int(x+y/10),y) for x in range(200)] for y in range(250)])
cv2.imshow("plot",img)

# =============================================================================
# 
# =============================================================================

#裁切圖片
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
cv2.imshow("winnie",img)
img_slice = img[80:600,500:]
cv2.imshow("img_slice_singal winnie",img_slice)
print(img.shape)

img_slice2 = img[0:(img.shape[0]*2//3),0:(img.shape[1]*2//3)]
cv2.imshow("img_slice_singal winnie",img_slice2)

# =============================================================================
# 
# =============================================================================

#縮放相片
# 新圖片物件=cv2.resize(圖片物件,(新寬度,新高度))
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
img_resize = cv2.resize(img,(5000,5000))
cv2.imshow("winnie resize",img_resize)

# =============================================================================
# 
# =============================================================================

#翻轉照片
# cv2.flip(圖片物件,翻轉方向) #翻轉方向 0垂直 1水平 -1水平+垂直
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
img_flip = cv2.flip(img,1)
cv2.imshow("winnie flip",img_flip)

# =============================================================================
# 
# =============================================================================

#旋轉照片
#method1
# 變換矩陣 = cv2.getRotationMatrix2D((旋轉中心的X座標,旋轉中心的Y座標),旋轉角度,放大倍數)
#建立完"變換矩陣"後，使用warpAffine()來選轉圖片物件
#cv2.warpAffine(圖片物件,變換矩陣,(新圖片的寬,新圖片的高))
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
aff_matrix = cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2),90,1)
img_rotate = cv2.warpAffine(img,aff_matrix,(img.shape[1],img.shape[0]))
cv2.imshow("winnie rotate",img_rotate)

#method2
#cv2.rotate(圖片物件,旋轉參數) 0-2 0=90 1=180 2=270 or -90
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
img_rotate2 = cv2.rotate(img,2)
cv2.imshow("winnie rotate2",img_rotate2)

# =============================================================================
# 
# =============================================================================

#轉換圖片的色彩空間
#RGB to HSV L*a*b
#cv2.cvtColor(圖片物件,色彩空間轉換參數)
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
img_convert = cv2.cvtColor(img,cv2.COLOR_BGR2Luv)
cv2.imshow("winnie convert",img_convert)

# =============================================================================
# 
# =============================================================================

#圖片反轉(負片效果)
# cv2.bitwise_not(圖片物件)
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
img_invert = cv2.bitwise_not(img)
cv2.imshow("winnit_invert",img_invert)

# =============================================================================
# 
# =============================================================================
#圖片二值化處理
# cv2.threshold(圖片物件,閥值,像素最大值,二值化類型參數)
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
thr, img_binary =cv2.threshold(img,190,255,cv2.THRESH_BINARY)

cv2.imshow("winnin_binary",img_binary)

# =============================================================================
# 
# =============================================================================
#遮罩處理
#cv2.bitwise_and(圖片1,圖片2,mask=遮罩圖片的路徑)
img = cv2.imread("C:/Users/wunyu/Pictures/466084.jpg")
mask = cv2.imread("C:/git-repo/python learning/F1378/F1378/Ch11_(OpenCV)/photo/mask.jpg")
mask = cv2.imread("C:/git-repo/python learning/F1378/F1378/Ch11_(OpenCV)/photo/mask.jpg",cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask,(img.shape[1],img.shape[0]))
img_masked =cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("mask",img_masked)

mask=cv2.bitwise_not(mask)
img_masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("mask",img_masked)

# =============================================================================
# 
# =============================================================================
#相片模糊
#cv2.blur(圖片,過濾器尺寸) #平均模糊
#cv2.medianBlur(圖片,過濾器尺寸) #中位數模糊
#cv2.GaussianBlur(圖片,過濾器尺寸,X軸高斯分布標準差,Y軸高斯分布標準差)

img=cv2.imread('C:/git-repo/python learning/F1378/F1378/Ch11_(OpenCV)/photo/sample.jpg')
img_blur=cv2.blur(img,(20,20),0)
img_medianBlur=cv2.medianBlur(img,7)
img_GaussBlur=cv2.GaussianBlur(img,(49,49),0)


cv2.imshow("normal",img) #正常照片
cv2.imshow("blur",img_blur) #平均模糊
cv2.imshow("median",img_medianBlur) #中位數模糊
cv2.imshow("GaussianBlur",img_GaussBlur) #高斯模糊

# =============================================================================
# 
# =============================================================================

img=cv2.imread("C:/git-repo/python learning/F1378/F1378/Ch11_(OpenCV)/photo/sample2.jpg")
img_denoised = cv2.fastNlMeansDenoisingColored(img,h=3)
cv2.imshow("Normal",img)
cv2.imshow("Denoised",img_denoised)







