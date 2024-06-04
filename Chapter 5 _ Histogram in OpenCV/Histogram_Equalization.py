import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('../Data_image_from_opencv/flower2.webp',0)

# Equalize histogram image
hist = cv2.equalizeHist(img)

# Merge image
res = np.hstack((img, hist))

# Show image
cv2.imshow('Original Image', res)
cv2.waitKey()
cv2.destroyAllWindows()