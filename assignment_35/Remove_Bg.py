import cv2
import matplotlib.pyplot as plt
import numpy as np

logo = cv2.imread('microsoft.png')
logo = cv2.cvtColor(logo,cv2.COLOR_BGR2RGBA)
plt.imshow(logo)
plt.show()
bg =np.array([87 , 83 , 82])

rows , cols, bands = logo.shape
for i in range(rows):
    for j in range(cols):
        if logo[i,j][0]==87 and logo[i,j][1] == 83 and logo[i,j][2]==82:
            logo[i,j][3]=0
           
plt.imshow(logo)
plt.show()
cv2.imwrite('logo.png',logo)