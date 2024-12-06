import cv2 as cv

def change_Res(capture,width=1920,height=1080):
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture(0)

change_Res(capture)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Resolution',frame)
    if cv.waitKey(20) & 0xFF == 'd':
        break

capture.release()
cv.destroyAllWindows()
