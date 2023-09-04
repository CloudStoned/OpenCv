import cv2 as cv
import numpy as np 

blank_img = np.zeros((500,500,3), dtype='uint8') # uint8 datatype of an image 
# cv.imshow('Blank',blank_img)
 

# 1. paint the image a certain color
# idx of array here is the pixels in an image 
# blank_img[200:300,300:400] = 0,255,0 # all pixels 
# cv.imshow("Green",blank_img)

# 2. draw a rectangle
# cv.rectangle(blank_img,(0,0), (250,250), (0,255,0), thickness=2) # (img,(position of the figure), (width,height), (Color))
# cv.rectangle(blank_img, (0,0), (blank_img.shape[1]//2, blank_img.shape[0]//2), (0,255,0), thickness=-1) # thickness -1 to fill the shape with prefered color
# cv.imshow("Rect",blank_img)

# 3. draw a circle
# cv.circle(blank_img, (blank_img.shape[1] // 2, blank_img.shape[0] // 2), 40, (0,0,255),thickness=-1)
# cv.imshow("Cirlce",blank_img)

 # 4. draw a line 
# cv.line(blank_img, (100,20), (blank_img.shape[1]//2, blank_img.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow("Line",blank_img)

# 5. write text on an image
cv.putText(blank_img, "Hello", (50,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),thickness=2) # imge, text, location, font, fontscale, color
cv.imshow("hello",blank_img)


# img = cv.imread('Pic/kaguyacat.jpg')
# cv.imshow('KAGUYA',img)
cv.waitKey(0)