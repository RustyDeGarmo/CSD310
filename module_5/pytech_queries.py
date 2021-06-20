"""
Rusty DeGarmo
Professor Sampson
Database Development and Use
19 June 2021
"""
#import mongodb
from pymongo import MongoClient

#connect to database
url ="mongodb+srv://admin:admin@cluster0.aqzbi.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

docs = db.students.find({})

print("-- DLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

doc = students.find_one({"student_id": 1007})

print(f'Student ID: {doc["student_id"]}')
print(f'First Name: {doc["first_name"]}')
print(f'Last Name: {doc["last_name"]}')




