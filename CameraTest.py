import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(10,100)

img = cv2.imread("resources/teste.jpeg")
kernel = np.ones((5,5), np.uint8 )
while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(img, (7, 7), 0)
    img_canny = cv2.Canny(img, 40, 40)
    img_dilated = cv2.dilate(img_canny,kernel, iterations=1)
    img_erode = cv2.erode(img_dilated,kernel, iterations=5)

    cv2.imshow("canny", img_canny)
    # cv2.imshow("dilated", img_dilated)
    # cv2.imshow("erode", img_erode)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
