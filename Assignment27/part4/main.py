import cv2
import numpy as np
image=cv2.imread("TV.jpg")
a=image.shape[0]
b=image.shape[1]
writer =cv2.VideoWriter('Tv_noice.mp4', cv2.VideoWriter_fourcc(*'XVID'),30,(b,a))
while True:
    image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    noice=np.random.random((194,260))*255
    noice=np.array(noice,dtype=np.uint8)
    image[53:247,85:345]=noice
    image=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    writer.write(image)
    cv2.imshow("result",image)

    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
writer.release()