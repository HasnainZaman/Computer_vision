import cv2 as cv
import numpy as np

# Open web cam 
cap = cv.VideoCapture(0)

while(True):
    (ret,frame)=cap.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (tresh,binary)=cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)


    cv.imshow("OriginalCam",frame)
    cv.imshow("Gray_Scale",gray_frame)
    cv.imshow("Binary",binary)
    if cv.waitKey(1) & 0XFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()