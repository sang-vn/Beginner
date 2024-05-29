import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/sudoku.png')

canny = cv2.Canny(img, 0, 255)

plt.subplot(1,2,1), plt.imshow(img,cmap='gray')
plt.title('ORIGINAL'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2), plt.imshow(canny,cmap='gray')
plt.title('CANNY'), plt.xticks([]), plt.yticks([])

plt.show()