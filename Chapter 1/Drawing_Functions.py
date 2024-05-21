import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creat a black image
image = np.full((512,512,3), (0,0,255), np.uint8)

# Draw line
image = cv2.line(image, (0,0), (200, 100), (255,255,0), 2, 2)

# Draw circle
image = cv2.circle(image, (300,300), 50, (0,255,0), 2, cv2.LINE_4)

# Draw rectangle
image = cv2.rectangle(image, (100,100), (300, 300), (255,0,0), 2)

# Draw ellipse
image = cv2.ellipse(image, (200, 200), (100, 50), 360, 0, 360, (255, 255,255), 2)

# Insert Text
font = cv2.FONT_ITALIC
image = cv2.putText(image, "Hello",(50, 400), font, 2, (0, 0, 0), 2)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()