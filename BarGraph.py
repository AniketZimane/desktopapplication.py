import matplotlib.pyplot as plt
import mysql.connector as c
mydb=c.connect(host='localhost',
                user='root',
                password='123456',
                database='student1')
result=mydb.is_connected()
select_query="select status from attendance_db"
select1_query="select name from attendance_db"
mycursor = mydb.cursor()
mycursor.execute(select_query)
datavalue=mycursor.fetchall()
mycursor.execute(select1_query)
dataname=mycursor.fetchall()
# mark=[data[0][0]]
mydata=list()
mark=list()
print(dataname)
if dataname:
    for i in dataname:
        for j in i:
            mydata+=i


if datavalue:
    for i in datavalue:
        for j in i:
            mark+=i


plt.bar(mydata,mark)
plt.xlabel("Courses")
plt.ylabel("Student Attendance")
plt.title("Student Attendance Graph")
plt.show()

# print("connection establish")
# x=["Java","Python","CSS","C","C++"]
# h=[100,90,80,120,50]
# plt.bar(x,h)
# plt.xlabel("Courses")
# plt.ylabel("Student Attendance")
# plt.title("Student Attendance Graph")
# plt.show()