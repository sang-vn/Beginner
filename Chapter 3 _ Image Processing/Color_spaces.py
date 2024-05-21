import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

cv2.namedWindow('Color_spaces', cv2.WINDOW_NORMAL)

def nothing(x):
    pass

# Creat Trackbar to set range of HSV color
cv2.createTrackbar('LH', 'Color_spaces',0,150, nothing)
cv2.createTrackbar('LS', 'Color_spaces',0,180, nothing)
cv2.createTrackbar('LV', 'Color_spaces',0,150, nothing)
cv2.createTrackbar('UH', 'Color_spaces',150,255, nothing)
cv2.createTrackbar('US', 'Color_spaces',180,255, nothing)
cv2.createTrackbar('UV', 'Color_spaces',150,255, nothing)


while True:

    # Take each frame
    ret, frame = cap.read()

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH', 'Color_spaces')
    ls = cv2.getTrackbarPos('LS', 'Color_spaces')
    lv = cv2.getTrackbarPos('LV', 'Color_spaces')
    uh = cv2.getTrackbarPos('UH', 'Color_spaces')
    us = cv2.getTrackbarPos('US', 'Color_spaces')
    uv = cv2.getTrackbarPos('UV', 'Color_spaces')

    # define range of blue color in HSV
    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()