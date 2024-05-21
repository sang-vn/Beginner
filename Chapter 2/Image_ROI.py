import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../Images/jump.jpg')

# truy cap vung roi theo cu phap image[y1:y2, x1:x2]
ball = image[110:200, 470:570]
image[110:200, 200:300] = ball

cv2.imshow('Image when changing', image)
cv2.waitKey()
cv2.destroyAllWindows()