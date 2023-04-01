import time
import datetime
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector as c
from tkinter import *
from tkinter import messagebox

def scancard():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
#def scanQr():
    # with open('mydeta.text')as f:
    #     mydatalist=f.read().title()
    while True:
        success,img=cap.read()
        for barcode in decode(img):
        #print(barcode.data)
            mydata=barcode.data.decode('utf-8')
            printdata='Attendance maked successfully'
        # print(mydata)
            stringdata=str(mydata)

            newsplitdata = stringdata.split('\n')
        # print(newsplitdata)

            newList = list()
            for i in newsplitdata:
            # print(i)
                if i:
                    first = i.split(':')
                    newList += first
        # print(newList)

            time.sleep(5)

            mydb = c.connect(
                host='localhost',
                user='root',
                password='123456',
                database='project_01'
            )
            mycursor = mydb.cursor()
            stu ="present"
            now=datetime.datetime.now()
            curdate=now.strftime("%d-%m-%y")
            curtime=now.strftime("%H:%M:%S")

            insert_sql_query = "INSERT INTO students_attendance(Student_id,Name,Department,Year,Gender,Date,Time,Status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (newList[1], newList[3], newList[5], newList[7], newList[13], curdate, curtime, stu)
        # val = (values,curdate,curtime,stu)
            mycursor.execute(insert_sql_query, values)
            mydb.commit()

            pts=np.array([barcode.polygon],np.int32)
            pts=pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            pts2=barcode.rect
            cv2.putText(img,printdata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
        cv2.imshow('result',img)
        k=cv2.waitKey(1)
        if k%256==27:
            messagebox.showinfo("Closing scanner")
            break


    #"select * from Login where [username]='" & TextBox1.Text & "' and[password]='" & TextBox2.Text & "'"
    # Button(root, text="QR Generate",
    #    font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=600,
    #                                                                          width=180,
    #                                                                          height=30)
    #
scancard()
