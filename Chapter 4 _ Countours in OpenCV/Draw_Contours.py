import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/pic4.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, th1 = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img_gray,60,255,cv2.THRESH_BINARY_INV)
Adaptive_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
thresh = cv2.bitwise_and(th1,th2)
contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# find Perimeter
cnt = contours[1]
P = cv2.arcLength(cnt,True)
print('Perimeter: ' + str(P))

# find Area
S = cv2.contourArea(cnt)
print('Area: ' + str(S))

# draw Contours
img = cv2.drawContours(img, cnt, -1, (0,0,255), 3)

cv2.imshow('Image', img)
cv2.imshow('Image2', th2)
cv2.imshow('Image3', img_gray)
# cv2.imshow('Image4', thresh)
cv2.waitKey()
cv2.destroyAllWindows()