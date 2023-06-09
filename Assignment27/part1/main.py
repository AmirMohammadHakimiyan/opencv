import cv2

import numpy
cap=cv2.VideoCapture(0)
_,frame =cap.read()
satr = frame.shape[0]
sotoon = frame.shape[1]
writer=cv2.VideoWriter("result.mp4",cv2.VideoWriter_fourcc(*'XVID'),30,(sotoon,satr))
while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    satr = frame.shape[0]
    sotoon = frame.shape[1]
    w=frame[satr*2//5:satr*3//5,sotoon*2//5:sotoon*3//5]
    kernel=numpy.ones((41,41))/1661
    re_image=cv2.filter2D(frame, -1,kernel)
    re_image[satr*2//5:satr*3//5,sotoon*2//5:sotoon*3//5]=w
    cv2.rectangle(re_image,(sotoon*2//5,satr*2//5),(sotoon*3//5,satr*3//5),0,4)
    re_image[satr*2//5:satr*3//5,sotoon*2//5:sotoon*3//5]
    if numpy.average(w)>=160:
        color="white"
    elif numpy.average(w)<=90:
        color="black"
    else:
        color="gray"

    cv2.putText(re_image,color,(30,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,0,3)


    re_image=cv2.cvtColor(re_image,cv2.COLOR_GRAY2BGR)
    writer.write(re_image)
    cv2.imshow("result",re_image)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
writer.release()
