import mysql.connector as c
mydb=c.connect(host="localhost",
               user="root",
               password="123456",
               database="student1")
mycursor=mydb.cursor()
def insertImage(FilePath):
    with open(FilePath,"rb") as File:
        binarydata=File.read()
    sqlstatement="insert into images (Photo) values(%s)"
    print(binarydata)
    mycursor.execute(sqlstatement,(binarydata, ))
    mydb.commit()

def retriveImage(ID):
    sqlstatement2="select * from images where id='{0}'"
    mycursor.execute(sqlstatement2.format(str(ID)))
    myresult=mycursor.fetchone()[1]
    storefilepath="images/img{0}.jpg".format(str(ID))
    print(myresult)
    with open(storefilepath,"wb") as File:
        File.write(myresult)
        File.close()

print("1.Insert image\n 2.Read images")
choice=input()
if int(choice)==1:
    filepath=input("Enter file path:")
    insertImage(filepath)
elif int(choice)==2:
    userid=int(input("Enter id:"))
    retriveImage(userid)