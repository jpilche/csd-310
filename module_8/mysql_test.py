import mysql.connector #connection code
from mysql.connector import errorcode

conn = mysql.connector.connect(
    host="localhost",
    database="pysports",
    user="root",
    password="admin" 
)

cursor = conn.cursor()
cursor.execute("select * from team")

for row in cursor:
    print(row)