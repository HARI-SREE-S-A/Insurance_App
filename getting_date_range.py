from pymongo import MongoClient
from datetime import datetime, timedelta
​
client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
db = client["Insuarance_app"]
collection = db["customer_data"]
start_date = datetime(2023, 1, 31)
end_date = datetime(2023, 5, 30)
documents = collection.find({"Date": {"$gte": start_date, "$lte": end_date}})
​
for document in documents:
    print(document)
    date_str = document['Date'].strftime('%Y-%m-%d')
    date_object = datetime.strptime(date_str, '%Y-%m-%d')
    print(date_object)
​
