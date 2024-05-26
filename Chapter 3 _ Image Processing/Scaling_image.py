import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images/car.jpg')

img1 = cv2.resize(img, None,fx = 2,fy=2, interpolation=cv2.INTER_CUBIC)

# Or
height, width = img.shape[:2]
img2 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Image', img)
cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.waitKey()
cv2.destroyAllWindows()