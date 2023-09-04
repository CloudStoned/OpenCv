import cv2 as cv
import numpy as np 

img = cv.imread("Pic/jelly.png")

imghor = np.hstack((img, img))
imgver = np.vstack((img, img))


cv.imshow("hor",imghor)
cv.imshow("ver", imgver)
cv.waitKey(0)