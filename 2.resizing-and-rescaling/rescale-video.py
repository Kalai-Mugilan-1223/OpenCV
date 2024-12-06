import cv2 as cv

def frame_rescale(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture  = cv.VideoCapture('2.resizing-and-rescaling\\Videos\\cat.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('D&Wxleo',frame)
    resized_frame = frame_rescale(frame,0.65)
    cv.imshow('Resized',resized_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
