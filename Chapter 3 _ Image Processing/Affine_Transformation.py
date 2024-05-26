import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images/car.jpg')
rows, cols = img.shape[:2]

pst1 = np.float32([[50,50], [100,100], (50,100)])
pst2 = np.float32([[150,150],[200,150],[200,250]])

m = cv2.getAffineTransform(pst1, pst2)

img1 = cv2.warpAffine(img, m, (2*rows, 2*cols))

cv2.imshow("Origibal", img)
cv2.imshow("Image after translating", img1)

cv2.waitKey()
cv2.destroyAllWindows()