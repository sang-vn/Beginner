import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../../Images/clock.jpg')

b,g,r = cv2.split(image)
print(b,g,r)

img1 = cv2.merge((r,g,b))
cv2.imshow("Img1", img1)

img2 = cv2.merge((b,g,r))
cv2.imshow("Img2", img2)

cv2.waitKey()
cv2.destroyAllWindows()