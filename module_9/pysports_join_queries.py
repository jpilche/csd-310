import mysql.connector #connection code
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "admin",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
   

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")


except mysql.connector.Error as err:


    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
   

    db.close()