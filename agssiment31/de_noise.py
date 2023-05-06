import cv2
import numpy as np
noise=cv2.imread("input/xray_noisy.png",cv2.IMREAD_GRAYSCALE)
un_noise=np.zeros(noise.shape,dtype=np.uint8)
kernel=np.ones((3,3),dtype=np.uint8)/9
for sa in range(1,noise.shape[0]-1):
    for so in range(1,noise.shape[1]-1):
        box=noise[sa-1:sa+2,so-1:so+2]*kernel
        result=np.sum(box)
        un_noise[sa,so]=result
cv2.imshow("",un_noise)
cv2.waitKey()
cv2.imwrite("output/delete_noise3.jpg",un_noise)