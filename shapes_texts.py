import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.imread("resources/teste.jpeg")
# img[200:300,10:300]  = 255,0,0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (250, 350), 30, (255, 0, 0), 5)
cv2.putText(img, "iaeee", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 2.2, (150,150,0), 2)

cv2.imshow("image1", img)

cv2.waitKey(0)
