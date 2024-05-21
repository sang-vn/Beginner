import cv2
import numpy
import matplotlib.pyplot as plt

# Khởi tạo webcam
cap = cv2.VideoCapture(0)

# Set parameters for webcam
cap.set(3, 500)
cap.set(4, 500)

# Intial window to show images/videos
AutoWindow = 'Start with Videos'
cv2.namedWindow(AutoWindow, cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    cv2.imshow(AutoWindow, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Ok.jpg", frame)

# When everything done, release webcam
cap.release()
cv2.destroyAllWindows()