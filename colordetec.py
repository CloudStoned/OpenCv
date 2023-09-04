import cv2 as cv 
import numpy as np

def empty(a):
    pass

def stackImages(scale, imgArray):
    rows = len(imgArray) 
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv.resize(imgArray[x][y], (width, height))
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)

        blank_image = np.zeros((height, width, 3), np.uint8)
        hor = [blank_image] * rows

        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])

        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv.resize(imgArray[x], (width, height))
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)

        hor = np.hstack(imgArray)
        ver = hor

    if scale != 0:
        ver = cv.resize(ver, (int(ver.shape[1] / scale), int(ver.shape[0] / scale)))

    return ver

# Trackbar Values
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)

# SET THE NUMBERS TO GET THE DEFAULT VALUE OF 
# A MASK IMAGE for ex: 30,173,137,255,0,255

cv.createTrackbar("Hue Min", "TrackBars", 30, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 173, 179, empty)
cv.createTrackbar("Satu Min", "TrackBars", 137, 255, empty)
cv.createTrackbar("Satu Max", "TrackBars", 255, 255, empty)
cv.createTrackbar("Value Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Value Max", "TrackBars", 255, 255, empty)

while True:
    img = cv.imread("Pic/kaguyacat.jpg")
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    satu_min = cv.getTrackbarPos("Satu Min", "TrackBars")
    satu_max = cv.getTrackbarPos("Satu Max", "TrackBars")
    val_min = cv.getTrackbarPos("Value Min", "TrackBars")
    val_max = cv.getTrackbarPos("Value Max", "TrackBars")

    print(h_min, h_max, satu_min, satu_max, val_min, val_max)

    lower = np.array([h_min, satu_min, val_min])
    upper = np.array([h_max, satu_max, val_max])
    mask = cv.inRange(imgHSV, lower, upper)
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # Stack images horizontally
    stacked_img = stackImages(2, [[img, imgHSV], [mask, imgResult]])
    
    # cv.imshow("ORIGINAL",img)
    # cv.imshow("IMGHSV",imgHSV)
    # cv.imshow("IMGMASK",mask)
    # cv.imshow("IMGRESULT", imgResult)
    cv.imshow("Stacked Images", stacked_img)
    
    cv.waitKey(1)
