import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image , ImageDraw, ImageFont ,ImageOps
import arabic_reshaper


img = Image.open('1.jpg') 
plt.imshow(img)
plt.show()   
colors = ['red' , 'green' , 'blue']
for i,color in enumerate(colors):
    img_array = np.array(img)
    lum_img = img_array[:,:,i]
    plt.hist(lum_img.ravel(), bins=range(256),color = color)
plt.show()
cv2.imwrite("lum_img.jpg",lum_img)


img_eq = ImageOps.equalize(img) 
img_eq =  np.array(img_eq)
plt.imshow(img_eq)
plt.show()
cv2.imwrite("img_eq.jpg",img_eq)

for i,color in enumerate(colors):
    img_array_eq = np.array(img_eq)
    lum_img_eq = img_array_eq[:,:,i]
    plt.hist(lum_img_eq.ravel(), bins=range(256),color = color)
img_array_eq =  np.array(img_array_eq)
plt.show()
cv2.imwrite("img_array_eq.jpg",img_array_eq)


result = np.mean(img,axis=2)
plt.imshow(result,cmap='gray')
plt.show()
result =  np.array(result)
cv2.imwrite("result.jpg",result)

#Calculate histogram and show with plt.
plt.hist(result.ravel(), bins=range(256),color = color)
plt.show()


gray =img.convert("L")
gray_eq = ImageOps.equalize(gray) 
plt.imshow(gray_eq, cmap="gray" )
plt.show()
gray_eq =  np.array(gray_eq)
cv2.imwrite("gray_eq.jpg",gray_eq)

gray_array_eq = np.array(gray_eq)
plt.hist(gray_array_eq.ravel(), bins=range(256),color = color)
plt.show()
gray_array_eq =  np.array(gray_array_eq)
cv2.imwrite("gray_array_eq.jpg",gray_array_eq)