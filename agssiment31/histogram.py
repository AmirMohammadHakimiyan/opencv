import cv2
# import matplotlib
image=cv2.imread("input/REN.png",cv2.IMREAD_GRAYSCALE)
hist=cv2.calcHist([image],[0],None,[256],[0,256])
#       oryou can use down source code
# b=[]
# c=[]
# for i in range(256):
#     c.append(0)
# image=cv2.imread("input/REN.png",cv2.IMREAD_GRAYSCALE)
# for satr in range(image.shape[0]):
#     for sotoon in range(image.shape[1]):
#         for i in range(256):
#             if i==image[satr,sotoon]:
#                 b.append(i)
# for e in range(255):
#     for v in b:
#         if v==e:
#             c[e]+=1
print(hist.astype(int))