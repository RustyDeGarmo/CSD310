import mysql.connector

#connect to database
db= mysql.connector.connect(
	host="localhost",
	user="root",
	password= "rBillie-0928t",
	database= "outlandadventures"
)

#create a cursor
mycursor = db.cursor()

#create the trip table if it doesn't already exist and add data 
mycursor.execute ("CREATE TABLE IF NOT EXISTS trip (trip_id INT AUTO_INCREMENT PRIMARY KEY, \
destination_name VARCHAR(75), arrival_date VARCHAR(75), departure_date VARCHAR(75)) ")
sql = "INSERT INTO trip (destination_name, arrival_date, departure_date) VALUES (%s, %s, %s)"
val = [
 ("Africa", "02/01/2017", "02/10/2017"),
 ("Asia", "02/14/2017", "02/24/2017"),
 ("Southern Europe", "05/10/2017", "05/11/2017"),
 ("Africa", "05/21/2017", "05/31/2017"),
 ("Asia", "11/12/2017", "11/23/2017"),
 ("Southern Europe", "12/01/2017", "12/12/2017"),
 ("Asia", "02/03/2018", "02/14/2018"),
 ("Southern Europe", "03/05/2018", "03/15/2018"),
 ("Africa", "04/13/2018", "04/23/2018"),
 ("Southern Europe", "06/11/2018", "06/21/2018"),
 ("Asia", "07/21/2018", "07/31/2018")
 ]
mycursor.executemany (sql,val)
db.commit()

#create the supplies table if it doesn't exist and add data
mycursor.execute ("CREATE TABLE IF NOT EXISTS supplies (equipment_name VARCHAR(75), \
quantity_needed VARCHAR(75), equipment_cost VARCHAR (75), inventory_in_stock VARCHAR (75), \
trip_id VARCHAR(75), date_added varchar(10))")
sql = "INSERT INTO supplies (equipment_name, quantity_needed, equipment_cost, \
inventory_in_stock, trip_id, \
date_added) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
 ("A-E-01", "2", "15.00", "46", "1", "03/05/21"),
 ("A-E-02", "1", "35.00", "25", "1", "03/05/21"),
 ("A-E-03", "4", "70.00", "46", "1", "03/05/21"), 
 ("A-F-01", "1", "60.00", "21", "2", "03/05/21"),
 ("A-F-02", "1", "40.00", "24", "2", "03/05/21"),
 ("S-E-01", "2", "25.50", "20", "3", "03/05/21"),
 ("S-E-02", "2", "32.00", "32", "3", "03/05/21")
]
mycursor.executemany (sql,val)
db.commit ()

#create the guide table if it doesn't exist and add data
mycursor.execute ("CREATE TABLE IF NOT EXISTS guide (guide_id INT AUTO_INCREMENT PRIMARY KEY, \
first_name VARCHAR(75), last_name VARCHAR(75), trip_id VARCHAR(75))")
sql = "INSERT INTO guide (first_name, last_name, trip_id) VALUES (%s, %s, %s)"
val = [
 ("John", "MacNell", "1"), 
 ("D.B.", "Marland", "2"),
 ("John", "MacNell", "3"), 
 ("D.B.", "Marland", "4"),
 ("John", "MacNell", "5"), 
 ("D.B.", "Marland", "6")
]
mycursor.executemany (sql,val)
db.commit()

#create the customer table if it doesn't exist and add data
mycursor.execute("CREATE TABLE IF NOT EXISTS customer (customer_id INT AUTO_INCREMENT PRIMARY KEY, \
first_name VARCHAR (75), last_name VARCHAR(75), supplies VARCHAR (75), trip_id VARCHAR (75))") 
sql = "INSERT INTO customer (first_name, last_name, supplies, trip_id) VALUES (%s, %s, %s, %s)"
val = [
 ("Ana", "Lemus", "rented", "1"),
 ("Susan", "Brown", "bought", "1"),
 ("Luis", "Hernandez", "rented", "1"),
 ("Carter", "Morrison", "bought", "2"),
 ("Marco", "Martinez", "rented", "2"),
 ("Samuel", "Garcia", "rented", "2"),
 ("Luke", "Murphy", "rented", "3"),
 ("Zane", "Smith", "bought", "3"),
 ("Alec", "Williams", "rented", "3"),
 ("Matt", "Park", "rented", "3")
 ]
mycursor.executemany (sql,val)
db.commit()

#close the database
db.close()