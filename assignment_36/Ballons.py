import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ballons.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
low_hu = np.array([165,0,0]) 
upp_hu = np.array([180,255,255])
mask = cv2.inRange(img, low_hu, upp_hu)

plt.subplot(1,2,1)
img_rgb = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
plt.imshow(img_rgb)

plt.subplot(1,2,2)
plt.imshow(mask,cmap='gray')

plt.show()