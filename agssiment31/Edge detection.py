import cv2
import numpy as np
# write input\lion.png or input/spider.webp
image=cv2.imread("input\spider.webp",cv2.IMREAD_GRAYSCALE)
satr,sotoon=image.shape
picture=np.ones((satr,sotoon),dtype=np.uint8)

kernel=np.array([[-1,-1,-1],
                 [-1, 8,-1],
                 [-1,-1,-1]])
for sa in range(1,image.shape[0]-1):
    for so in range(1,image.shape[1]-1):
        box=image[sa-1:sa+2,so-1:so+2]
        result=np.abs(np.sum(box*kernel))
        picture[sa,so]=result

cv2.imshow("",picture)
cv2.waitKey()
cv2.imwrite("output/edge_detection_2.jpg",picture)
