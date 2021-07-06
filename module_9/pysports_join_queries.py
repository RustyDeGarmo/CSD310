'''
Rusty Degarmo
Professor Sampson
Database Development and Use
6 July 2021
'''

#imports
import mysql.connector
from mysql.connector import errorcode

#connect to server
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

#create a cursor
cursor = db.cursor()

#get the join
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM \
player INNER JOIN team ON player.team_id = team.team_id;")
output = cursor.fetchall()

#create some space and display the header
print()
print("-- DISPLAYING PLAYER RECORDS --")

#print all the things
for thing in output:
    print("Player ID: {}".format(thing[0]))
    print("First Name: {}".format(thing[1]))
    print("Last Name: {}".format(thing[2]))
    print("Team Name: {}".format(thing[3]))
    print()

#pause the window to view output
input("\n\nPress any key to continue... ")

#close up shop
db.close()

#my terminal copy/paste comment because I'm too lazy to type it out again if something else
#ends up on my clipboard
#py pysports_join_queries.py






