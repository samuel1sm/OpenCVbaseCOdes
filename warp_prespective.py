import cv2
import numpy as np

img = cv2.imread("resources/cartas.jpeg")

width, height = int(img.shape[0] / 2), int(img.shape[1] / 2)

img = cv2.resize(img, (height, width))

pts1 = np.float32([[192, 173], [359, 127], [367, 409], [543, 327]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matrix, (width,height))

cv2.imshow("image3", imgOutput)

cv2.waitKey(0)
