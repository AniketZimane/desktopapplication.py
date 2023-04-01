
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img=cv2.imread('2001170252.png')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#def scanQr():
with open('mydata.txt')as f:
    mydatalist=f.read().splitlines()
print(mydatalist)
while True:
    success,img=cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        mydata=barcode.data.decode('utf-8')
        printdata='Attendance maked successfully'
        print(mydata)
        if mydata in mydatalist:
            print("authorised person")
        else:
            print("unauthorised person")
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        cv2.putText(img,printdata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
    cv2.imshow('result',img)
    cv2.waitKey(1)

    #"select * from Login where [username]='" & TextBox1.Text & "' and[password]='" & TextBox2.Text & "'"

