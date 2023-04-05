from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
db = client["Insuarance_app"]
collection = db["customer_data"]
documents =collection.distinct("Date")



for document in documents:
    date_object = datetime.strptime(document, '%Y,%m,%d')
    print(date_object)
