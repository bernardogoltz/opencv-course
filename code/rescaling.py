# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:17:43 2022

@author: bernardogoltz
@title: rescaling and resizing
"""

import cv2 as cv 

path = 'C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Photos/cat_large.jpg'

img = cv.imread(path)
cv.imshow('Cat',img)


def change_resolution(width,height):
    # only works from live videos
    capture.set(3,width)
    capture.set(3,height)


def rescaleFrame(frame,scale = 0.75):
    # will work for images and videos
    width = int(frame.shape[0]*scale)
    height = int(frame.shape[1]*scale)
    
    dimensions = (width , height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img,scale = 0.1)
cv.imshow("RESZED IMAGE",resized_image)

capture = cv.VideoCapture('C:/Users/angel/OneDrive/Documentos/opencv-course/Resources/Videos/dog.mp4')
# reading videos 
while True: 
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
    
capture.release()
