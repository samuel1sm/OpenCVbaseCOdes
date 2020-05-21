import cv2
import numpy as np

img = cv2.imread("resources/cartas.jpeg")
width, height = int(img.shape[0] / 2), int(img.shape[1] / 2)
img = cv2.resize(img, (height, width))

hor = np.hstack((img,img))  
ver = np.vstack((img,img))

cv2.imshow("horizontal", hor)
cv2.imshow("vertical", ver)

cv2.waitKey(0)