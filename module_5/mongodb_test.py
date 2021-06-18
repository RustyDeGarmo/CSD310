#Rusty DeGarmo
#Professor Sampson
#Database Development and Use
#17 June 2021

from pymongo import MongoClient

url ="mongodb+srv://admin:admin@cluster0.aqzbi.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())



