import cv2
import numpy as np
building=cv2.imread("input/building.png",cv2.IMREAD_GRAYSCALE)
vertical_house=np.zeros(building.shape)*255
horizontal_house=np.zeros(building.shape)*255
kernel_vertical=np.array([[-1,0,1],
                          [-1,0,1],
                          [-1,0,1]])
kernel_horizontal=np.array([[-1,-1,-1],
                            [0,0,0],
                            [1,1,1]])
for sa in range(1,building.shape[0]-1):
    for so in range(1,building.shape[1]-1):
        box=building[sa-1:sa+2,so-1:so+2]*kernel_vertical
        result=np.sum(box)
        vertical_house[sa,so]=result
for sa in range(1,building.shape[0]-1):
    for so in range(1,building.shape[1]-1):
        box=building[sa-1:sa+2,so-1:so+2]*kernel_horizontal
        result=np.sum(box)
        horizontal_house[sa,so]=result

cv2.imshow("",vertical_house)
cv2.imshow("",horizontal_house)
cv2.waitKey()
cv2.imwrite("output/vertical_building.png",vertical_house)
cv2.imwrite("output/horizontal_building.png",horizontal_house)