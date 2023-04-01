import cv2
from tkinter import messagebox
cam=cv2.VideoCapture(0)
cv2.namedWindow("Capturing face....")
img_count=0
while True:
    ret,frame=cam.read()
    if not ret:
        messagebox.showinfo("message", "Pleae fill all the field")
        break
    cv2.imshow("test",frame)
    k=cv2.waitKey(1)
    if k%256==27:
        messagebox.showinfo("message", "Escaped key hit,closing window")
        break
    elif k%256==32:
         img_name="person{}.png".format(img_count)
         messagebox.showinfo("message", "Photo captured")

cam.release()
cam.destroyAllWindows()