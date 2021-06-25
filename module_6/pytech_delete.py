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
docs = myCollection.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop through the documents printing each in formatted version
for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()

#create a new student document
jim = {
        "student_id": 1010,
        "first_name": "Jim",
        "last_name": "Holden",
        }

#insert the new student document
jim_student_id = myCollection.insert_one(jim).inserted_id

#print insert statement
print("-- INSERT STATEMENTS --")
print(f'Inserted student record into the students collection with document_id {jim_student_id}')
print()

#create a query for the new document
myQuery = {"student_id": 1010}

#find the new document 
newDoc = myCollection.find_one(myQuery)

#print the updated information
print("-- DISPLAYING STUDENT TEST DOC --")
print(f'Student ID: {newDoc["student_id"]}')
print(f'First Name: {newDoc["first_name"]}')
print(f'Last Name: {newDoc["last_name"]}')
print()

#find the new student 1010 and delete the document
myCollection.delete_one(myQuery)

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#find the documents in the collection
#I'm not sure why I have to include this again here but it doesn't
#work otherwise. I never modified docs after my initial declaration above
#so I don't understand why I have to declare it again here. 
# 
# Can you explain?
docs = myCollection.find()

#loop through the documents printing each in formatted version
for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()



