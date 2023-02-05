try:
    db = mysql.connector.connect(**config)
    print("*\n Database user {} connected to MySQL on host {} with database {}".format(config["root"], config ["127.0.0.1"], config ["pysports"]))
    input ("\n\n Press any key to contine...")

except: mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid ")

    else if err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else
        print(err)

finally:
    db.close()