import cv2
import numpy as np
import matplotlib.pyplot as plt

x = np.uint8([250])
y = np.uint8([10])

print('x + y = ' + str(x+y))
print(cv2.add(x, y))