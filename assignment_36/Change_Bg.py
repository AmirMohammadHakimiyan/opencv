import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('SuperMan.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img)
back_ground=cv2.imread('1.jpg')

back_ground=cv2.resize(back_ground,[2048,1444])
back_ground = cv2.cvtColor(back_ground,cv2.COLOR_BGR2HSV)
H_b, S_b, V_b = cv2.split(back_ground)

H_new = H.copy()
S_new = S.copy()
V_new = V.copy()
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if V_new[i,j] > 90 :
            if 30< H[i,j] <80:
                H_new[i,j] = H_b[i,j]
                S_new[i,j] = S_b[i,j]
                V_new[i,j] = V_b[i,j]

result = cv2.merge((H_new,S_new,V_new))
result = cv2.cvtColor(result,cv2.COLOR_HSV2RGB)
plt.imshow(result)
plt.show()