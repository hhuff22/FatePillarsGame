from pymongo import MongoClient
client = MongoClient()
db = client["project1"]
charDataColl = db["characters"]

myquery = { "name": "Pylance" }

charDataColl.delete_one(myquery)