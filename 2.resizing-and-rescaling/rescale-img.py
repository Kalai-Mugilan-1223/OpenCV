import cv2 as cv

def frame_rescale(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



img = cv.imread('2.resizing-and-rescaling\\Images\\Kadisi Ulaga por x Big Dawgs.png')
cv.imshow('Big-Dawgs',img)

img_resized = frame_rescale(img,0.3)
cv.imshow('Resized_img',img_resized)

cv.waitKey(0)
