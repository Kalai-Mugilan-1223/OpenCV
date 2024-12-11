import cv2 as cv
import numpy as np

#Reading an image

img = cv.imread('5.image-transformations\\src\\img.jpg')
cv.imshow('Image',img)

#translating an image

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)

translated = translate(img,-50,100)
cv.imshow("Translated",translated)

#Rotating an Image

def rotate(img,angle,rotPoint = None):
    height,width = img.shape[:2]
    if rotPoint is None:
        rotPoint = width//2,height//2
    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotmat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated',rotated)

"""NOTE : Trying to rotate an rotated an image
will not be same as rotating the image for first time
for eg:
    Rotating the image directly to 90 deg angle produces diff result from rotating the image 
    2 times with 45 deg. The second method will rotate the image 45 def then it will take the 
    rotated image and rotate it again to 45 deg"""

#Resizing an Image
resized = cv.resize(img,(500,500),interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#for shrinking images use cv.INTER_AREA or default(no value)
#for enlarging image we can use cv.INTER_LINEAR or cv.INTER_CUBIC
#for INTER_CUBIC the time to respond will be higher with high quality


#Flipping an image
flip = cv.flip(img,0)
cv.imshow('Flipped',flip)

"""
0 -> Flips x - axis
1 -> Flips y - axis
-1 -> Flips both x and y - axis
"""

#cropping an image
crop = img[200:400,100:400]
cv.imshow('Crop',crop)
cv.waitKey(0)
