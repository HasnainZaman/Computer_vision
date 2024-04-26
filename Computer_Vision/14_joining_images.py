import numpy as np
import cv2 as cv


img= cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")
img=cv.resize(img,(480,720))
img1=cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")
img1=cv.resize(img,(480,720))

# stack 

hor=np.hstack((img,img1))
v_stack = np.vstack((img1,img))
v_stack = cv.resize(v_stack,(480,720))

#cv.imshow("Frame1",img)
cv.imshow("frame1",hor)

cv.imshow("frame2",v_stack)
cv.waitKey(0)
cv.destroyAllWindows()