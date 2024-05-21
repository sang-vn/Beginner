import cv2
import numpy
import matplotlib.pyplot as plt

# Imread images
image = cv2.imread("../Images\car.jpg")
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()