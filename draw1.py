import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8) # CREATE EMPTY PIC
print(img.shape) # check dimensions
# print(img)

img[:] = 255,0,0 # color the whole pic 
# img[100:255,300:512] = 255,0,0

# Resize
imgresize = cv.resize(img,(1000,500))
# print(imgresize.shape)

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3)
cv.rectangle(img,(0,0),(250,250), (0,0,255),cv.FILLED) # or desire thickness
cv.circle(img,(400,50),30,(255,255,0),3)
cv.putText(img, " OPEN CV ", (300,200), cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)

cv.imshow("img",img)


cv.waitKey(0)