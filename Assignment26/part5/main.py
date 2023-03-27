import cv2
import numpy

image=numpy.ones([500,500],dtype=numpy.uint8)*255

for i in range(100):
    image[i+160:i+170,i+160:i+170]=0
    image[160+i:170+i,360-i:370-i]=0

image[170:290,160:175]=0
image[170:290,355:370]=0
cv2.imshow("result",image)
cv2.waitKey()
cv2.imwrite("result.jpg",image)
