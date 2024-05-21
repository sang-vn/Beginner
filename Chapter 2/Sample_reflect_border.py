import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tạo một ảnh 5x5 để minh họa
img = np.array([[10, 20, 30, 40, 50],
                [60, 70, 80, 90, 100],
                [110, 120, 130, 140, 150],
                [160, 170, 180, 190, 200],
                [210, 220, 230, 240, 250]], dtype=np.uint8)

# Mở rộng biên của ảnh bằng BORDER_REFLECT
border_size = 1
img_with_border_reflect = cv2.copyMakeBorder(img,
                                             top=border_size,
                                             bottom=border_size,
                                             left=border_size,
                                             right=border_size,
                                             borderType=cv2.BORDER_REFLECT)

# Mở rộng biên của ảnh bằng BORDER_REFLECT_101
img_with_border_reflect_101 = cv2.copyMakeBorder(img,
                                                 top=border_size,
                                                 bottom=border_size,
                                                 left=border_size,
                                                 right=border_size,
                                                 borderType=cv2.BORDER_REFLECT_101)

# Hiển thị ảnh trước và sau khi thêm biên
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Ảnh gốc')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Ảnh với BORDER_REFLECT')
plt.imshow(img_with_border_reflect, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Ảnh với BORDER_REFLECT_101')
plt.imshow(img_with_border_reflect_101, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()

# In giá trị pixel của ảnh với biên để dễ theo dõi
print("Ảnh với BORDER_REFLECT:")
print(img_with_border_reflect)

print("Ảnh với BORDER_REFLECT_101:")
print(img_with_border_reflect_101)
