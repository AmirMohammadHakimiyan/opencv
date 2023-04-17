import cv2

first_leter=cv2.imread("input/leter_1.jpg",cv2.IMREAD_GRAYSCALE)
_,first_leter=cv2.threshold(first_leter,100,255,cv2.THRESH_BINARY_INV)

editer=cv2.imread("input/leter_2.jpg",cv2.IMREAD_GRAYSCALE)
_,editer=cv2.threshold(editer,100,255,cv2.THRESH_BINARY_INV)
result=first_leter-editer
_,result=cv2.threshold(result,100,255,cv2.THRESH_BINARY_INV)
cv2.imwrite("output/result_leter.jpg",result)