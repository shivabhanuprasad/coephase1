import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@123",
    database="Ace")
c=conn.cursor()
id=input("Enter your id to delete record from DB")
c.execute("delete from student where sid=%s",(id,))
conn.commit()
c.close()
conn.close()