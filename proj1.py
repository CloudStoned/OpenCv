import cv2 as cv 
import numpy as np 

# READ WEBCAM
frameWidth = 640
frameHeight = 480

capture = cv.VideoCapture(0) # number depends to your cameras
capture.set(3,frameWidth)
capture.set(4,frameHeight)
capture.set(10,150)

# list of colors that we want to detect 
# we need to set the min and max hue 

myColors = [ ] 




def findColor(img):
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV) # convert the image to hsv
    # lower = np.array([h_min, s_min, v_min ])
    # upper = np.array([h_max, s_max, v_max])
    # mask = cv.inRange(imgHSV, lower, upper)
    # cv.imshow("IMG",mask)





# Run the webcam 
while True:
    success, img = capture.read()
    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

