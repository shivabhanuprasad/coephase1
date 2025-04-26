import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@123",
    database="Ace")
c=conn.cursor()
sid=input("Enter your sid : ")
sname=input("Enter your sname : ")
city=input("Enter your city : ")
marks=input("Enter your marks : ")
c.execute("insert into Student (sid,sname,city,marks) values (%s,%s,%s,%s)",(sid,sname,city,marks))
conn.commit()
c.close()
conn.close()
