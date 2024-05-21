import cv2
import numpy as np

image = cv2.imread("../Images/jump.jpg")

# px = image[100,100]
# print(px)
#
# blue = image[100,100,0]
# print(blue)
#
# image[100,100] = [255,255,255]
# print(image[100,100])

# Accessing red pixel
print(image.item(10,10,2))
image.itemset((10,10,2),100)
print(image.item(10,10,2))