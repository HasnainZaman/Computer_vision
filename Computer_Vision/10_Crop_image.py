import cv2 as cv 
import numpy as np


img = cv.imread("G:\Open_cv\Computer_Vision\Recource\picture1.jpg")
img = cv.resize(img,(720,1080))

crop=img[0:450,0:500]





cv.imshow("Original_image",img)
cv.imshow("Crop_image",crop)

cv.waitKey(0)
cv.destroyAllWindows()