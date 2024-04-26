import cv2 as cv
import numpy as np


# cap video

cap = cv.VideoCapture(0)
cap.set(10,100)



cap.set(3,1080)# set width
cap.set(4,720)# set height


while(True):
    ret,frame = cap.read()
    if ret ==True:
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()