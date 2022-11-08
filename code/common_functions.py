# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:38:58 2022

@author: bernardogoltz

@title: 5 essential functions in OpenCV.

"""

import cv2 as cv

path = 'C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Photos/cat.jpg'

img = cv.imread(path)
cv.imshow("cat",img)

# converting to grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray cat",gray)

# blur 
blur = cv.GaussianBlur(img,(0,10),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

# edge cascade --> canny edge
boston = cv.imread('C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Photos/park.jpg')


#reducing the edges by blurring the image 

boston_blur = cv.GaussianBlur(boston,(3,3),cv.BORDER_DEFAULT)

canny = cv.Canny(boston_blur,175,200)

cv.imshow('normal boston',boston)
cv.imshow("canny" , canny)
gray_boston = cv.cvtColor(boston , cv.COLOR_BGR2GRAY)

cv.imshow("Gray Boston",gray_boston)

blur_boston = cv.GaussianBlur(gray_boston,(0,0),cv.BORDER_DEFAULT)

canny_boston = cv.Canny(blur_boston,0,50)
cv.imshow("blur_boston",canny_boston)

# dilate
dilated = cv.dilate(canny_boston,(7,7),iterations = 3)
cv.imshow("Dilated",dilated)


# Resize 
resized = cv.resize(img,(300,300))
cv.imshow("image resized",resized)




