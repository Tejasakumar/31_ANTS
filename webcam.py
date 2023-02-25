import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

#img=cv.imread('Kodikon/ImagesK/demo.jpg')

capture=cv.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:
    success,img=capture.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        cv.imwrite('abc.png',img)
       

    cv.imshow('result',img)
    cv.waitKey(1)

