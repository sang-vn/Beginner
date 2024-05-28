import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/LinuxLogo.jpg')

kenel = np.ones((5,5), np.uint8)
kenel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

erosion = cv2.erode(img, kenel,iterations=1)

dilate = cv2.dilate(img, kenel, iterations=1)

open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kenel)

close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kenel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kenel)

top_hat1 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kenel1)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kenel)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kenel)

cv2.imshow('images', top_hat1)
cv2.imshow('Image2', top_hat)
cv2.waitKey()
cv2.destroyAllWindows()