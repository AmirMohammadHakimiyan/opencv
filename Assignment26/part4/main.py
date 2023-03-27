import cv2
import numpy
image=numpy.ones([600,600],dtype=numpy.uint8)*255
color=255
for satr in range(600):

    for sotoon in range(600):
        image[satr,sotoon]=color
    color-=1
    if satr%2==0:
        color+=1
    if color<0:
        color+=1

cv2.imshow("result",image)
cv2.waitKey()
cv2.imwrite("result.jpg",image)