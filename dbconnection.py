import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@123",
    database="Ace")
print("Database cconnected !")
conn.close()