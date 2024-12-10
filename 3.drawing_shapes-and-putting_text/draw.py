"""NOTE :  This Programming file contains different methods to draw or create different shapes, every method is highlighed with comments above
            So, to check each shapes function , except that particular one comment others"""

import cv2 as cv
import numpy as np

#creating blank and displaying
blank = np.zeros((500,500),dtype = 'uint8') # 'uint8' is a dataype of image 
cv.imshow('Blank' , blank)

#changing the color of the blank

blank = np.zeros((500,500,3),dtype = 'uint8')
blank[:] = 0,255,0
cv.imshow('Colored - Blank' , blank)

#changing color of the particular portion

blank [200:300 , 300:400] = 0,255,255
cv.imshow('Portion' , blank)

#Drawing a rectangle

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=3)
cv.imshow('Rectangle without fill',blank)

#Drawing a rectangle with fill


cv.rectangle(blank,(blank.shape[1]//2,blank.shape[0]//2),(500,500),(0,0,255),thickness=-1)
cv.imshow('Rectangle with fill',blank)

#Note : To fill the shape you can either use thickness = -1 or cv.FILLED

#Drawing a Circle 

cv.circle(blank,(250,250),40,(255,0,0),thickness=3)
cv.imshow('Circle',blank)

#Drawing a Line

cv.line(blank,(0,0),(500,500),(255,255,255),thickness=3)
cv.imshow('Straight Line',blank)

#Writing a Text 
cv.putText(blank,'Hello World',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(200,255,200),2)
cv.imshow('Text',blank)

cv.waitKey(0)
