import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../Images/clock.jpg')

BLUE = [255,0,0]

replicate = cv2.copyMakeBorder(image, 20,20,20,20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image, 20,20,20,20,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image, 20,20,20,20,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(image, 20,20,20,20,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(image, 20,20,20,20,cv2.BORDER_CONSTANT, value=(100,100,0))

plt.subplot(231), plt.imshow(image, 'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()