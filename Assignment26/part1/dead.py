import cv2

class Dead():
    def __init__(self,image):
        self.image=cv2.imread(image)
        self.image_2=cv2.cvtColor(self.image,cv2.COLOR_RGB2GRAY)
    def make(self,zekhamat): 
        for i in range(40):

            self.image_2[0+i:2+i,40-i:50+zekhamat-i]=0
        for i in range(10+zekhamat):
            self.image_2[40+i:42+i,0:10+zekhamat-i]=0
        cv2.imshow("result",self.image_2)
# print(image.shape)
        cv2.waitKey()
        cv2.imwrite("result.jpg",self.image_2)