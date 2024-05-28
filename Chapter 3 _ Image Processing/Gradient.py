import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/sudoku.png')

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_8U,1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

plt.subplot(2,2,1), plt.imshow(img,cmap='gray')
plt.title('ORIGINAL'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2), plt.imshow(laplacian,'gray')
plt.title('LAPLACIAN'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3), plt.imshow(sobelx,'gray')
plt.title('SOBELX'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4), plt.imshow(sobely, 'gray')
plt.title('SOBELY'), plt.xticks([]), plt.yticks([])

plt.show()