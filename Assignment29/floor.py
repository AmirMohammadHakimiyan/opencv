import cv2

editer=cv2.imread("input/img_floor1.jpg")

floor=cv2.imread("input/img_floor2.jpg")

home=cv2.imread("input/img_floor3.jpg")
editer_2=editer
editer_1=editer
_,editer_1=cv2.threshold(editer_1,100,255,cv2.THRESH_BINARY)
editer_1=editer//255
new_floor=editer_1*floor

_,editer_2=cv2.threshold(editer_2,100,255,cv2.THRESH_BINARY_INV)
editer_2//=255
new_home=editer_2*home

result=cv2.add(new_home,new_floor)

cv2.imwrite("output/NEW_HOME.jpg",result)