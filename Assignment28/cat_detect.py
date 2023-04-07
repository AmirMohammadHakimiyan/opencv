import cv2
image=cv2.imread("cats.jpeg")
image_gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cat_detect=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalcatface.xml")
faces=cat_detect.detectMultiScale(image_gray)
number=0
for face in faces:
    number+=1
    x,y,w,h=face
    cv2.rectangle(image,(x,y),(x+w,y+h),0,4)
cv2.imshow("result",image)
cv2.waitKey()
print("count:",number)
cv2.imwrite("output/result_cat.jpg",image)