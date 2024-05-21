import cv2
import numpy as np

# Duoc dung de kiem tra xem gia tri cua bien co thay doi khong. Neu co thay doi thi goi ham creatTrackbar
def nothing(x):
    pass


# Creat black image and a window
image = np.zeros((500,500,3), np.uint8)
cv2.namedWindow("Trackbar", cv2.WINDOW_NORMAL)

# Creat trackbar for RGB channel
cv2.createTrackbar('Red', 'Trackbar',0, 255, nothing)
cv2.createTrackbar("Green", "Trackbar",0, 255, nothing)
cv2.createTrackbar("Blue", "Trackbar",0, 255, nothing)

# Creat On/Off functions
switch = "O : OFF\n1 : ON"
cv2.createTrackbar(switch, "Trackbar", 0, 1, nothing)



while True:
    cv2.imshow("Trackbar", image)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    r = cv2.getTrackbarPos("Red", 'Trackbar')
    g = cv2.getTrackbarPos("Green", 'Trackbar')
    b = cv2.getTrackbarPos("Blue", 'Trackbar')
    s = cv2.getTrackbarPos(switch, 'Trackbar')

    if s == 0:
        image[:] = 0

    if s == 1:
        image[:] = [b, g, r]

cv2.destroyAllWindows()
