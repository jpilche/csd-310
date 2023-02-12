import mysql.connector #connection code
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "admin",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

# INSERT
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()
    
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")
    db.commit()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")

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

# UPDATE
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor1 = db.cursor()
    
    cursor1.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    db.commit()
    cursor1.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")

    players1 = cursor1.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")

    for j in players1:
        print(f"\n Player ID: {j[0]}\n First Name: {j[1]}\n Last Name: {j[2]}\n Team Name: {j[3]}\n")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

# DELETE
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor2 = db.cursor()
    
    cursor2.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    db.commit()
    cursor2.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")

    players2 = cursor2.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")

    for k in players2:
        print(f"\n Player ID: {k[0]}\n First Name: {k[1]}\n Last Name: {k[2]}\n Team Name: {k[3]}\n")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()