import cv2 as cv
import numpy as np

# Open web cam 
cap = cv.VideoCapture(0)

while(cap.isOpened()):
    ret,frame =cap.read()
    if ret==True:
        # to disply cam
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0XFF ==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()