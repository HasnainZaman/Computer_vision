import cv2 as cv
import numpy as np


img= cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")

# function to set size 

img=cv.resize(img,(300,500))

# gray imag

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# binary image
(thresh,binary) = cv.threshold(gray_img ,127,255,cv.THRESH_BINARY)

# blured image 

blured_imag = cv.GaussianBlur(img,(7,7),0)


# Edge detection 
edge_dect = cv.Canny(img,48,48)



cv.imshow("Original",img)
cv.imshow("Gray_image",gray_img)
cv.imshow("Black_image",binary)
cv.imshow("Blured",blured_imag)
cv.imshow("Edge_detection",edge_dect)

cv.waitKey(0)
cv.destroyAllWindows()