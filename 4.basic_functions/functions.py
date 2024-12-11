import cv2 as cv

#Reading an image

img = cv.imread('4.basic_functions\\src\\img.jpg')
cv.imshow('Image',img)

#Converting Image to Grayscale

grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',grayImage)

#Blurring an Image 

blurred = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blurred Image',blurred)

#Creating Edge Cascade
#Outlines the Image and provides the outut
#uses canny function to outline the image

canny = cv.Canny(img,200,100)
cv.imshow('Edged Image',canny)

#Dilating the Image
#Dilation is used to remove the noise from the canny images
#It is used to join the broken parts

dilated = cv.dilate(canny,(7,7),iterations = 1)
cv.imshow('Dilated Image',dilated)

#Eroding the Image
#Eroding is followed by dilating 
#Erodig is also used to removes small whites & noises
#It Detaches 2 connected objects

erosion = cv.erode(dilated,(3,3),iterations = 1)
cv.imshow("Eroded Image",erosion)

#Resizing an Image
resized = cv.resize(img,(540,675))
cv.imshow('Resized',resized)

#Cropping an Image
#This Involves in cropping a particular portion of the image and displays it

crop = img[75:500,200:500]
cv.imshow('Cropped-Image',crop)



cv.waitKey(0)
