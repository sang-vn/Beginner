import cv2
import numpy
import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo webcam
cap = cv2.VideoCapture(0)

# Set parameters for webcam
# cap.set(3, 1000)
# cap.set(4, 600)

# Intial window to show images/videos
AutoWindow = 'Start with Videos'
cv2.namedWindow(AutoWindow, cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    black = np.zeros((height, width, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    contours, hierarchy = cv2.findContours(adaptive,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    image = cv2.drawContours(black, contours, -1, (0,255,0),2)
    cv2.imshow(AutoWindow, image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Ok.jpg", image)

# When everything done, release webcam
cap.release()
cv2.destroyAllWindows()