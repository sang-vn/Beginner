import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("../../Images/car.jpg")
image2 = cv2.imread("../../Images/jump.jpg")

# print(image1.dtype)
# print(image2.dtype)

# image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Cach 1: Rezise images
# image1 = cv2.resize(image1, (200,200))
# image2 = cv2.resize(image2, (200,200))

# Cach 2: Cat anh
image1 = image1[0:200,0:200]
image2 = image2[0:200,0:200]

# d𝑠𝑡 = 𝛼 · 𝑖𝑚𝑔1 + 𝛽 · 𝑖𝑚𝑔2 + 𝛾
dst1 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
dst2 = cv2.add(image1, image2)

plt.subplot(121), plt.imshow(dst1), plt.title('DST 1')
plt.subplot(122), plt.imshow(dst2), plt.title('DST 2')
plt.show()