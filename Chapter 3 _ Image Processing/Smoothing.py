import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/aloeR.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Average smoothing
blur1 = cv2.blur(img, (5, 5))

# Gaussian Filter
blur2 = cv2.GaussianBlur(img, (5,5), 0)

# Median Smoothing  
blur3 = cv2.medianBlur(img, 5)

# Bilateral Filtering
blur4 = cv2.bilateralFilter(img, 9, 75, 75)

images = [img, blur1, blur2, blur3, blur4]
title = ['Original', 'Average Smoothing', 'Gaussian Filter', 'Median Filter', 'Bilateral Filter']

for i in range(5):
    plt.subplot(2, 3, i+1), plt.title(title[i])
    plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()