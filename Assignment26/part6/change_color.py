import cv2
# class Change_color():
def Change_color(name,image):
    image_1=cv2.imread(image)
    image_2=cv2.cvtColor(image_1,cv2.COLOR_RGB2GRAY)
    satr,sotoon=image_2.shape
    for i in range(satr):
        for g in range(sotoon):
            if image_2[i,g]<=127:
                color=255-image_2[i,g]
                image_2[i,g]=color
            else:
                color=128-(image_2[i,g]-127)
                image_2[i,g]=color
    cv2.imshow(name,image_2)
    cv2.waitKey()

    cv2.imwrite(name,image_2)
