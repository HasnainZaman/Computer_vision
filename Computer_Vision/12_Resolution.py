import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)


# set resolution 
def FHD():
    cap.set(3,1920)
    cap.set(4,1080)


def HD_R():
    cap.set(3,1080)
    cap.set(4,720)

# HD_R()
FHD()
while (True):
    ret,frame = cap.read()
    if ret==True:
        cv.imshow("Camera",frame)
        if cv.waitKey(1) & 0XFF ==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()