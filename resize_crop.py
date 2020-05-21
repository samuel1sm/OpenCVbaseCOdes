import cv2
import numpy as np

img = cv2.imread("resources/teste.jpeg")
print(img.shape)
imgResize = cv2.resize(img, (300, 200))

imgCropped = img[0:200, 200:500]
cv2.imshow("image",img)
# cv2.imshow("image2",imgResize)
cv2.imshow("image3",imgCropped)

cv2.waitKey(0)