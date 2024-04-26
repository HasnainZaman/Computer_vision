# import libraries
import cv2 as cv
import numpy as np


video = cv.VideoCapture("G:\Open_cv\Computer_Vision\Recource\Video.mp4")

if(video.isOpened()==False):
    print("Error to open video")

# read video frame by frame

while(video.isOpened()):
    ret,frame = video.read()
    if ret==True:
        # disply the frame 
        cv.imshow("frame",frame)
        if cv.waitKey(0) &  0xFF == ord('q'):
            break
        else:
            break
video.release()
cv.destroyAllWindows()
