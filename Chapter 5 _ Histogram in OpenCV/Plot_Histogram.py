import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/basketball1.png')

# plot by Matplotlib
# plt.hist(img.ravel(),256,[0,256]), plt.show()

# plot by OpenCV
hist = cv2.calcHist(img, channels=[2], mask=None, histSize=[256],ranges=[0,256])
# plt.plot(hist, color='green')
plt.xlim([0,256])
plt.show()


