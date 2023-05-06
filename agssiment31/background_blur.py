import cv2
import numpy as np
image=cv2.imread("input/flower_input.jpg",cv2.IMREAD_GRAYSCALE)
_,image_2=cv2.threshold(image,170,255,cv2.THRESH_BINARY)

kernel=np.ones((5,5))/25
for satr in range(1,image_2.shape[0]-1):
    for sotoon in range(1,image.shape[1]-1):
        box=image_2[satr-1:satr+2,sotoon-1:sotoon+2]
        box=np.sort(box,axis=None)

        image_2[satr,sotoon]=box[4]
flower=(image_2//255)*image
for _ in range(10):
    for satr in range(2,image.shape[0]-2): 
        for sotoon in range(2,image.shape[1]-2):        
            box=image[satr-2:satr+3,sotoon-2:sotoon+3]*kernel
            average=np.sum(box)
            image[satr,sotoon]=average
one=np.ones(image.shape)
one_2=np.ones(image.shape)*-1
_,z=cv2.threshold(image_2,170,255,cv2.THRESH_BINARY_INV)
back_ground=image*(z//255)
image=np.add(back_ground,flower)
cv2.imshow("",image)
cv2.waitKey()
cv2.imwrite("output/back_ground.jpg",image)