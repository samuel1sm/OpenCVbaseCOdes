import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("hue min", "TrackBars", 0, 179, lambda a: a)
cv2.createTrackbar("hue max", "TrackBars", 11, 179, lambda a: a)
cv2.createTrackbar("Sat min", "TrackBars", 161, 255, lambda a: a)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, lambda a: a)
cv2.createTrackbar("Val min", "TrackBars", 0, 255, lambda a: a)
cv2.createTrackbar("Val max", "TrackBars", 103, 255, lambda a: a)

while True:
    img = cv2.imread("resources/cartas.jpeg")
    width, height = int(img.shape[0] / 2), int(img.shape[1] / 2)
    img = cv2.resize(img, (height, width))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("hue max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val max", "TrackBars")
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imageResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("normal", img)
    # cv2.imshow("filtro", imgHSV)
    # cv2.imshow("mask", mask)
    # cv2.imshow("imageResult", imageResult)

    imgStack = stackImages(0.6, [[img,imgHSV], [mask,imageResult]])
    cv2.imshow("imageResult", imgStack)


    cv2.waitKey(1)
