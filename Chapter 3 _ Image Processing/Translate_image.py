import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images/car.jpg')
rows, cols = img.shape[:2]

m = np.float32([[1,0,100],[0,1,50]])

img1 = cv2.warpAffine(img, m, (cols+100, rows+50))

cv2.imshow("Origibal", img)
cv2.imshow("Image after translating", img1)

cv2.waitKey()
cv2.destroyAllWindows()