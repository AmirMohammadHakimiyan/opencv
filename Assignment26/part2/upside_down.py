import cv2
import numpy as np
class Upside_down():
    def __init__(self,image):
        self.image=cv2.imread(image)
        self.image_2=cv2.cvtColor(self.image,cv2.COLOR_RGB2GRAY)
        satr,sotoon=self.image_2.shape
        self.image_3=np.zeros([satr,sotoon],dtype=np.uint8)
        self.image_4=np.zeros([satr,sotoon],dtype=np.uint8)
        for i in range(satr):
            values=satr-i
            for g in range(sotoon):
                self.image_3[values-1,g]=self.image_2[i,g]
        for i in range(sotoon):
            values_2=sotoon-i
            for g in range(satr):
                self.image_4[g,values_2-1]=self.image_3[g,i]
    def make(self):    
        cv2.imshow("result",self.image_4)
        cv2.waitKey()
    def save(self):
        cv2.imwrite("result.jpg",self.image_4)