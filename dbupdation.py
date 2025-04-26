import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@123",
    database="Ace")
c=conn.cursor()
marks=input("Enter your marks : ")
sid=input("Enter your sid : ")
c.execute("Update Student set marks=%s where sid=%s",(marks,sid))
conn.commit()
c.close()
conn.close()