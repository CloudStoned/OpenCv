import cv2 as cv

img = cv.imread("Pic/shapes.png")
# imgResize = cv.resize(img, (500,500))

cv.imshow("IMG", img)
# cv.imshow("RESIZE",imgResize)
cv.waitKey(0)

