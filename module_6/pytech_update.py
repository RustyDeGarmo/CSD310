"""
Rusty DeGarmo
Professor Sampson
Database Development and Use
24 June 2021
"""
#import mongodb
from pymongo import MongoClient

#connect to database
url ="mongodb+srv://admin:admin@cluster0.aqzbi.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
myCollection = db.students

#find the documents in the collection
docs = db.students.find({})

print("-- DLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop through the documents printing each in formatted version
for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()

#find the document to be updated and specify the value to update
myQuery = {"student_id": 1007}
myUpdate = {"$set" : {"last_name": "Pesci"}}

#update the value
myCollection.update_one(myQuery, myUpdate)

#find the first student 
doc = myCollection.find_one()

#print the updated information
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print(f'Student ID: {doc["student_id"]}')
print(f'First Name: {doc["first_name"]}')
print(f'Last Name: {doc["last_name"]}')
print()