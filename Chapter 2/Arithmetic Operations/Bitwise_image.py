import cv2
import numpy as np
import matplotlib.pyplot as plt

# Doc anh
img1 = cv2.imread('../../Images/Logo_opencv.png')
img1 = cv2.resize(img1, (100,100))

img2 = cv2.imread('../../Images/Messi5.jpg')

# Creat ROI
rows, cols, channel = img1.shape
roi = img2[0:rows, 0:cols]

# Creat mask
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img2_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# Take only region of logo from logo image
img1_fg = cv2.bitwise_and(img1, img1, mask = mask)

# Put logo in ROI
dst = cv2.add(img2_bg, img1_fg)

img2[0:rows, 0:cols] = dst

cv2.imshow('res', mask_inv)
cv2.waitKey()
cv2.destroyAllWindows()