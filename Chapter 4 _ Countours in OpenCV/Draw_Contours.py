import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/LinuxLogo.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150,255, 0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

img = cv2.drawContours(img, contours, -1, (0,0,255), 3)

cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()