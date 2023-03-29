import cv2
import random

frame=cv2.imread("download.jpg")
frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
rows=frame.shape[0]
cols=frame.shape[1]
writer = cv2.VideoWriter("reseeultttt.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols,rows))
class Snow():
    def __init__(self,satr,sotoon):
        self.satr=satr
        self.sotoon=sotoon
    def run(self):
        self.satr+=1
snows=[]

while True:
    sotoon=random.randint(1,frame.shape[1]-1)
    snow=Snow(1,sotoon)
    snows.append(snow)
    for i in snows:
        i.run()
        if i.satr>=frame.shape[0]:
            i.satr-=2
        frame[i.satr,i.sotoon]=255
    writer.write(frame)
    cv2.imshow("result",frame)
    frame=cv2.imread("download.jpg")
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
writer.release()