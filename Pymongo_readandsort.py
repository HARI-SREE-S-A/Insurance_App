import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
db = client["Insuarance_app"]
collection = db["customer_data"]

# sort documents by the "date" field in ascending order
documents = collection.find().sort("Date", 1)

#for document in documents:
    #print(document)

# sort documents by the "date" field in descending order
documents = collection.find().sort("Date", 1)

for document in documents:
    print(document)

# sort documents by the "date" field using a datetime object
date_filter = datetime.strptime("05-04-2023", "%d-%m-%Y")
documents = collection.find({"Date": {"$gte": date_filter}}).sort("Date", 1)

for document in documents:
    print(document)

