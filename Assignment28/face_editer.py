import cv2
import keyboard
import numpy as np
cap=cv2.VideoCapture(0)
sticer=cv2.imread("input/sticer.png")
smile=cv2.imread("input/smile.png")
number=0
sticer_2=sticer
smile_2=smile
while True:
    # sticeron face
    _,frame=cap.read()
    fram_gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    if keyboard.is_pressed("1"):
        number=1
    elif keyboard.is_pressed("2"):
        number=2
    
    def sticer():
        sticer=sticer_2
        detect=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")
        faces=detect.detectMultiScale(fram_gray,1.3)
        for face in faces:
            x,y,w,h=face
            place=frame[y-10:y+h+10,x-10:x+w+10]
            sticer=cv2.resize(sticer,(w+20,h+20))
            for i in range(w+20):
                for g in range(h+20):
                    if sticer[i,g,0]==0 or sticer[i,g,1]==0 or sticer[i,g,2]==0:
                        sticer[i,g]=place[i,g]
        frame[y-10:y+h+10,x-10:x+w+10]=sticer
    
    if number==1:
        sticer()
    
        
            
    cv2.imshow("result",frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

