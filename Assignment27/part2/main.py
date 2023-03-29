import cv2

image=cv2.imread("bat.jpg")
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
_,image=cv2.threshold(image,150,255,cv2.THRESH_BINARY_INV)
satr,sotoon=image.shape
cv2.putText(image,"BATMAN",(430,500),cv2.FONT_HERSHEY_COMPLEX,1,255,4)

cv2.imshow("result",image)
cv2.waitKey()

cv2.imwrite("result_batman.jpg",image)