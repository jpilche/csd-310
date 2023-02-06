import mysql.connector #connection code
from mysql.connector import errorcode

conn = mysql.connector.connect(
    host="localhost",
    database="pysports",
    user="root",
    password="admin" 
)

cursor = conn.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")

print('-- DISPLAYING TEAM RECORDS --')

for row in cursor:
    #print(row[2])
    print('Team ID: ', row[0]) 
    print('Team Name: ', row[1])
    print('Mascot: ', row[2])
    print(' ')

cursor1 = conn.cursor()
cursor1.execute("SELECT player_id, first_name, last_name, team_id FROM player")

print('-- DISPLAYING PLAYER RECORDS --')

for row in cursor1:
    print('Player ID: ', row[0]) 
    print('First Name: ', row[1])
    print('Last Name: ', row[2])
    print('Team ID: ', row[3])
    print(' ')