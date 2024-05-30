import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Data_image_from_opencv/pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creat Thresh
ret, thresh = cv2.threshold(gray, 150,255,cv2.THRESH_BINARY_INV)

kenel = np.ones((3,3),np.uint8)
close_image = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kenel)

# Creat contours
contours, _ = cv2.findContours(close_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Set min, max area
min_area = 1000
max_area = 1000

# Take contour in [min, max]
filtered_contours = [cnt for cnt in contours if min_area<cv2.contourArea(cnt)]



for cnt in filtered_contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int32(box)
    img = cv2.drawContours(img, [box], -1, (0, 0, 255), 2)

    #  Creat Extreme Points
    left_most = tuple(cnt[cnt[:,:,0].argmin()][0])
    right_most = tuple(cnt[cnt[:, :, 0].argmax()][0])
    top_most = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottom_most = tuple(cnt[cnt[:, :, 1].argmax()][0])
    print(left_most), print('\n')
    img = cv2.circle(img,left_most,3,(0,255,0),-1)
    img = cv2.circle(img, right_most, 5, (150, 255, 200), -1)
    img = cv2.circle(img, top_most, 7, (100, 255, 50), -1)
    img = cv2.circle(img, bottom_most, 9, (0, 255, 150), -1)

#     x,y,w,h = cv2.boundingRect(cnt)
#     img = cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255),3)


# cnt = filtered_contours[0]
#
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int32(box)




cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()