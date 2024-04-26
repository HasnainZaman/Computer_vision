import cv2 as cv
import numpy as np

# capture a camra 

cap = cv.VideoCapture(0)
def hd_720():
    cap.set(3,1080)
    cap.set(4,720)

hd_720()

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

out = cv.VideoWriter("recorded_video.avi",cv.VideoWriter_fourcc('M',"J","P","G"),30,(frame_width,frame_height))

while(True):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()