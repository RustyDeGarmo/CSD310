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

#testing
#print(students)

joe = {
        "student_id": 1007,
        "first_name": "Joe",
        "last_name": "Schmoe",
        }

paul = {
        "student_id": 1008,
        "first_name": "Paul",
        "last_name": "Walker",
        }

john = {
        "student_id": 1009,
        "first_name": "John",
        "last_name": "Cena",
        }

students_list = [joe, paul, john]
    
joe_student_id = students.insert_one(joe).inserted_id
paul_student_id = students.insert_one(paul).inserted_id
john_student_id = students.insert_one(john).inserted_id

ids = [joe_student_id, paul_student_id, john_student_id]

print("-- INSERT STATEMENTS --")

print(f'Inserted student record {joe["first_name"]} {joe["last_name"]} into the students collection with document_id {joe_student_id}')
print(f'Inserted student record {paul["first_name"]} {paul["last_name"]} into the students collection with document_id {paul_student_id}')
print(f'Inserted student record {john["first_name"]} {john["last_name"]} into the students collection with document_id {john_student_id}')

#I was trying to create an iterable to go through these insert statements
#automatically but I'm out of time and I haven't figured it out yet