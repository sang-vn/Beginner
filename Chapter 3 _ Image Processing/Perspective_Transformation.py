import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/sudoku.png')
rows, cols = img.shape[:2]

pst1 = np.float32([[74,85], [490,70], [35,512],[518,518]])
pst2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

m = cv2.getPerspectiveTransform(pst1,pst2)

img1 = cv2.warpPerspective(img, m, (400,400))

cv2.imshow("Original", img)
cv2.imshow("Image after translating", img1)

cv2.waitKey()
cv2.destroyAllWindows()