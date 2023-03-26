import numpy
import cv2
image=numpy.zeros([600,600],dtype=numpy.uint8)
values=0
values_2=0
for g in range(8):
    if g%2==0:
        values=0
    else:
        values=75
    for i in range(4):
        image[values:values+75,values_2:values_2+75]=255
        values+=150
    values_2+=75
    
cv2.imshow("result",image)
cv2.waitKey()
cv2.imwrite("result.jpg",image)