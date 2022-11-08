# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:44:12 2022

@author: bernardogoltz
"""

import cv2 as cv
import numpy as np 


blank = np.zeros((500,500,3),dtype = 'uint8')

img = cv.imread('C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Photos/cats.jpg')

cv.imshow('Blank',blank)
cv.imshow('Cats',img)

blank[:] = 0,255,0
cv.imshow('Green',blank)

# draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,250,0),thickness = 2)
cv.imshow('Rectangle',blank)

# draw a circle
cv.circle(blank,(250,250),100,(0,0,255),thickness = 8)
cv.imshow('Circle',blank)

# draw a line 
cv.line(blank,(0,0),(500,500),(255,255,255),thickness = 3)
cv.imshow('lINE',blank)

# put some text 
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.2,(0,255,255),thickness = 1)
cv.imshow('Text',blank)

