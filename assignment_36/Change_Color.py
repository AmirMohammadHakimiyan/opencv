import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watermelon.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img)

H_new = H.copy()
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if 10< H[i,j] <90 :
            H_new[i,j] += 130
        if H[i,j] <15 or H[i,j]>150:
            H_new[i,j] += 60

result = cv2.merge((H_new,S,V))
result = cv2.cvtColor(result,cv2.COLOR_HSV2RGB)
plt.imshow(result)
plt.show()

img = cv2.imread('spiderman.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img)

H_new = H.copy()
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if 70< H[i,j] <150 :
            H_new[i,j] -= 81
        if H[i,j] <15 or H[i,j]>150:
            H_new[i,j] += 60

result = cv2.merge((H_new,S,V))
result = cv2.cvtColor(result,cv2.COLOR_HSV2RGB)
plt.imshow(result)
plt.show()