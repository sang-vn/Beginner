import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/gradient.png')

ret1, thresh1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img, 127,255,cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)

titles = ['ORIGINAL','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for x in range(6):
    plt.subplot(2,3,x+1),plt.imshow(images[x],'gray')
    plt.title(titles[x])
    plt.xticks([]),plt.yticks([])
plt.show()