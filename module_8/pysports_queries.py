'''
Rusty Degarmo
Professor Sampson
Database Development and Use
4 July 2021
'''

#imports
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "Rusty",
    "password": "sBillie-0928l",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

print()
print("-- DISPLAYING TEAM RECORDS --")

cursor.execute("SELECT team_id, team_name, mascot FROM team;")
teams = cursor.fetchall()

for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print()


print("-- DISPLAYING PLAYER RECORDS --")

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()


for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

input("\n\nPress any key to continue...")



db.close()

#py pysports_queries.py




