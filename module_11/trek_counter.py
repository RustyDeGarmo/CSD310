import mysql.connector

#connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "rBillie-0928t",
    database= "outlandadventures"
)

#create a cursor
cursor = db.cursor()

#Count how many treks were to Africa     
cursor.execute('SELECT COUNT(destination_name) FROM trip WHERE destination_name = "Africa";')
info = cursor.fetchall()

print()
print("-- DISPLAYING AFRICA TREK RECORDS --")
print(f"Number of treks to Africa: {info[0][0]}")
print()

#Count how many treks were to Asia   
cursor.execute('SELECT COUNT(destination_name) FROM trip WHERE destination_name = "Asia";')
info = cursor.fetchall()

print("-- DISPLAYING ASIA TREK RECORDS --")
print(f"Number of treks to Asia: {info[0][0]}")
print()

#Count how many treks were to Southern Europe
cursor.execute('SELECT COUNT(destination_name) FROM trip WHERE destination_name = "Southern Europe";')
info = cursor.fetchall()

print("-- DISPLAYING SOUTHERN EUROPE TREK RECORDS --")
print(f"Number of treks to Southern Europe: {info[0][0]}")
print()

#close the database
db.close()