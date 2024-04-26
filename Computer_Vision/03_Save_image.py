# load the libraries
import cv2 as cv
import numpy as np


# read the image 
imag = cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")
imag= cv.resize(imag,(300,500))


# convert into Gray Scale
gray_imag = cv.cvtColor(imag,cv.COLOR_BGR2GRAY)

# save gray scale

cv.imwrite("gray_image.jpg",gray_imag)

# convert into Binary

(thresh,binary)=cv.threshold(gray_imag,127,255,cv.THRESH_BINARY)

cv.imwrite("Binary_image.jpg",binary)
# show the image

cv.imshow("Original_Image",imag)
cv.imshow("Gray",gray_imag)
cv.imshow("Black And White",binary)

# set wait key

cv.waitKey(0)

# destroy windows
cv.destroyAllWindows()