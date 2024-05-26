import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images/car.jpg')
rows, cols = img.shape[:2]

# m = np.float32([[45,0,0],[0,45,0]])

m = cv2.getRotationMatrix2D((cols/2, rows/2), 90,1)

img1 = cv2.warpAffine(img, m, (rows, cols))

cv2.imshow("Origibal", img)
cv2.imshow("Image after translating", img1)

cv2.waitKey()
cv2.destroyAllWindows()