import cv2 as cv
import numpy as np


# read video 

video = cv.VideoCapture("Computer_Vision/Recource/Video.mp4")



# show video 
while(True):
    ret,frame =video.read()
    # convert into gray scale
    gray_video =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret==True:
        cv.imshow("fram",gray_video)
        if cv.waitKey(0) & 0XFF ==ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()



