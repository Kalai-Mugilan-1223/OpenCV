import cv2 as cv

capture  = cv.VideoCapture('1.read-images-videos\\Videos\\cat.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('cat',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
