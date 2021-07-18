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

#Count how many customers rented equipment        
cursor.execute('SELECT COUNT(supplies) FROM customer WHERE supplies = "rented";')
info = cursor.fetchall()

print()
print("-- DISPLAYING CUSTOMER RENTAL RECORDS --")
print(f"Number of customers who rented equipment: {info[0][0]}")
print()

#Count how many customers purchased equipment        
cursor.execute('SELECT COUNT(supplies) FROM customer WHERE supplies = "bought";')
info = cursor.fetchall()

print("-- DISPLAYING CUSTOMER PURCHASE RECORDS --")
print(f"Number of customers who purchased equipment: {info[0][0]}")
print()


#close the database
db.close()