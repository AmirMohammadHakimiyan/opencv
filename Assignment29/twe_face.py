import cv2
image_1=cv2.imread("input/woman.jpg")
image_1=cv2.resize(image_1,[300,300])
image_2=cv2.imread("input/man.jpg")
image_2=cv2.resize(image_2,[300,300])
for i in range(5):
    result=cv2.add(image_1//(i+1),image_2//2)
    cv2.imwrite(f"output/pic{i+2}.jpg",result)