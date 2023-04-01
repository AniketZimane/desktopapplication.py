import pyscreenshot
image=pyscreenshot.grab(bbox=(200,200,1000,1000))#x1,x2,y1,y2 y1=width y2=height
image.show()
image.save("Identycard/img1.png")
