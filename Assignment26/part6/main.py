# import cv2
import threading
import change_color
th_2=threading.Thread(target=change_color.Change_color,args=["result_2.jpg","2.jpg"])
th_1=threading.Thread(target=change_color.Change_color,args=["result_1.jpg","1.jpg"])
th_1.start()
th_2.start()
