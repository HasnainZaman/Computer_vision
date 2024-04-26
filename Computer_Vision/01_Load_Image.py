import cv2 as cv
import numpy as np

# Read the image
imag= cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")


# resize the image

imag=cv.resize(imag,(300,500))


# disply the image

cv.imshow("image",imag)


cv.waitKey(0)
cv.destroyAllWindows()