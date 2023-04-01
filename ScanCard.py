import mysql.connector as c
mydb=c.connect(host='localhost',
               user='root',
               password='123456',
               database='student1')
mycursor=mydb.cursor()
stringval='Student Id:2001170252,Student Name:Aniket Zimane,Student Department:Computer Engineering,Student Year:2019,' \
       'Student Address:A/P Shivapur Tal-Kudal Dist-Sindhudurg 416519'
splitdta=stringval.split(':')
stringval=stringval.split(',')
# print(stringval)
newList=list()
for i in stringval:
        # print(i)
        if i:
            first=i.split(':')
            newList+=first
# print(newList)
query="INSERT INTO mydb2(Student_Id,Student_Name,Student_Department,Student_Year,Student_Address)VALUES(%s,%s,%s,%s,%s)"
values=(newList[1],newList[3],newList[5],newList[7],newList[9])
print(values)
mycursor.execute(query,values)
mydb.commit()
print("Record inserted...")