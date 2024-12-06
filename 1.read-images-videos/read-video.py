import cv2 as cv

capture  = cv.VideoCapture('D:\\code-tools\\Code\\Python\\OpenCV\\read-images-videos\\Videos\\Leo x deadpool_mixdown_1.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Garudan',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()