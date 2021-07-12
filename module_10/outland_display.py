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

#Get all customer info and print        
cursor.execute("SELECT customer_id, first_name, last_name, supplies,trip_id FROM customer")
info = cursor.fetchall()

print("-- DISPLAYING CUSTOMER RECORDS --")
for customer in info:
    print("Customer ID: {}".format(customer[0]))
    print("First Name: {}".format(customer[1]))
    print("Last Name: {}".format(customer[2]))
    print("Supplies: {}".format(customer[3]))
    print("Trip ID: {}".format(customer[4]))
    print()
    print()


#Get guide info and print
cursor.execute("SELECT guide_id, first_name, last_name, trip_id FROM guide")
info = cursor.fetchall()

print("-- DISPLAYING GUIDE RECORDS --")
for guide in info:
    print("Guide ID: {}".format(guide[0]))
    print("First Name: {}".format(guide[1]))
    print("Last Name: {}".format(guide[2]))
    print("Trip ID: {}".format(guide[3]))
    print()
    print()

#Get supply info an print
cursor.execute("SELECT equipment_name, quantity_needed, equipment_cost, inventory_in_stock, \
trip_id,date_added FROM supplies")
info = cursor.fetchall()

print("-- DISPLAYING SUPPLY RECORDS --")
for supply in info:
    print("Equipment Name: {}".format(supply[0]))
    print("Quantity Needed: {}".format(supply[1]))
    print("Equipment Cost: {}".format(supply[2]))
    print("Inventory: {}".format(supply[3]))
    print("Trip ID: {}".format(supply[4]))
    print("Date Added: {}".format(supply[5]))
    print()
    print()

#Get trip info and print
cursor.execute("SELECT trip_id, destination_name, arrival_date,departure_date FROM trip")
info = cursor.fetchall()

print("-- DISPLAYING Trip RECORDS --")
for trip in info:
    print("Trip Id: {}".format(trip[0]))
    print("Destination Name: {}".format(trip[1]))
    print("Arrival Date: {}".format(trip[2]))
    print("Departure Date: {}".format(trip[3]))
    print()
    print()

#close the database
db.close()