# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:52:12 2022

@author: bernardogoltz
"""

#importing open cv 
import cv2 as cv 

path = 'C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Photos/cat.jpg'

img = cv.imread(path)

#cv.imshow('cat',img)

capture = cv.VideoCapture('C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Videos/dog.mp4')
# reading videos 
while True: 
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
    
capture.release()
