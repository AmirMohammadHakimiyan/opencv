import cv2
import numpy as np
image=np.ones([700,1400],dtype=np.uint8)
for i in range(5):
    min=350*i
    image[1:-1,min:min+175]+=20
cv2.rectangle(image,(1370,670),(30,30),255,4)
cv2.rectangle(image,(210,700*3//4),(30,700//4),255,4)
cv2.rectangle(image,(1370,700*3//4),(1190,700//4),255,4)
cv2.line(image,(700,670),(700,30),255,4)
cv2.circle(image,(700,350),90,255,4)
cv2.circle(image,(700,350),9,255,18)
cv2.imshow("Football",image)
cv2.waitKey()
cv2.imwrite("output/football.jpg",image)