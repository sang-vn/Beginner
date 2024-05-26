import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/sudoku.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Global thresholding
ret1, th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
th1 = cv2.cvtColor(th1, cv2.COLOR_GRAY2RGB)

# Otsu's thresholding
ret2, th2 = cv2.threshold(img, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th2 = cv2.cvtColor(th2, cv2.COLOR_GRAY2RGB)

# Otsu's thresholding after blur by Gauccian
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv2.threshold(blur, 0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
th3 = cv2.cvtColor(th3, cv2.COLOR_GRAY2RGB)

plt.subplot(1,4,1), plt.imshow(img1), plt.title('Original'), plt.xticks(), plt.yticks()
plt.subplot(1,4,2), plt.imshow(th1), plt.title('Global thresh'), plt.xticks(), plt.yticks()
plt.subplot(1,4,3), plt.imshow(th2), plt.title("Otsu's Thresh"), plt.xticks(), plt.yticks()
plt.subplot(1,4,4), plt.imshow(th3), plt.title("Otsu's after Bluring"), plt.xticks(), plt.yticks()

plt.show()