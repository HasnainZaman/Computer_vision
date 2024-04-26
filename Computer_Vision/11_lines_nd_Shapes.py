import cv2 as cv 
import numpy as np


img = np.zeros((500,500,3),np.uint8)
img2=np.ones((300,300,3),np.uint8)

img[:]=255,255,120
img2[150:230,100:200]=255,255,120

# Draw Line

cv.line(img,(0,0),(230,230),(25,255,12),3)

# draw rectangle

cv.rectangle(img2,(20,20),(50,60),(25,75,125),cv.FILLED)
cv.imshow("black",img)
cv.imshow("White",img2)

cv.waitKey(0)
cv.destroyAllWindows()