from datetime import datetime

from bson import ObjectId
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime, timedelta

output = str({'_id': ObjectId('6433ed1f698041ea2df2b537'), 'name': 'namw0', 'ph': 0, 'address': 'address00',
              'vehicle_number': 'KL99AA1111', 'Date':(2023, 4, 11, 0, 0)})

app = Flask(__name__)


def data_base_full():
    try:
        client = MongoClient("mongodb+srv://test:harvis30@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
        print("perfect")
        db = client["Insuarance_app"]
        collection = db["customer_data"]
        documents = collection.find()
        return documents
    except Exception as e:
        print("failed connection" + str(e))
def duration_sort(d1,d2):
    try:
        client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
        print("perfect")
        db = client["Insuarance_app"]
        collection = db["customer_data"]
        start_date = d1
        end_date = d2
        documents = collection.find({"Date": {"$gte": start_date, "$lte": end_date}})

        for document in documents:
            #print(document)
            date_str = document['Date'].strftime('%Y-%m-%d')
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
    except Exception as e:
        print("failed connection" + str(e))
        return document# ,date_object


def create_entry(name,address,ph,vehicle_number,Date):
    try:
        client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
        print("perfect")
        db = client["Insuarance_app"]
        collection = db["customer_data"]
        document = {
            "name": name,
            "ph": ph,
            "address": address,
            "vehicle_number": vehicle_number,
            "Date": Date
                      }
        res = collection.insert_one(document)
    except Exception as e:
        print("failed connection" + str(e))
    return {"entry":"success"}


def edit_existing_data(id,label,value):
    try:
        client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
        print("perfect")
        db = client["Insuarance_app"]
        collection = db["customer_data"]
        collection.update_one({"_id": id}, {"$set": {label:value}})


    except Exception as e:
        print("failed connection" + str(e))
    return {"update":"success"}


def delete_existing_data(id):
    try:
        client = MongoClient("mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority")
        print("perfect")
        db = client["Insuarance_app"]
        collection = db["customer_data"]
        result = collection.delete_one({"_id": ObjectId(id)})
        return {(result.deleted_count, "document deleted")}
    except Exception as e:
        print("failed connection" + str(e))






@app.get("/viewall")
def view_all():
    out = data_base_full()
    return out, 201
@app.post("/duration")
def duration_set()
    date = request.get_json()
    d1 = datetime.strptime(date["d1"], '%Y,%m,%d')
    d2 = datetime.strptime(date["d2"],'%Y,%m,%d')
    out = duration_sort(d1,d2)
    return out,201
@app.post("/new_entry")
def new_entry():

    data = request.get_json()
    name = str(data["name"])
    address = str(data["address"])
    ph = int(data["ph"])
    vehicle_number = data["vehicle"]
    date = str(data["date"])
    Date = datetime.strptime(date, '%Y,%m,%d')

    create_entry(name,address,ph,vehicle_number,Date)
    return {"update : successfully"},201

@app.post("/edit_existing")
def edit_existing(_id,label,value):
    data = request.get_json()
    id = data["_id"]
    label = data["label"]
    value = data["value"]
    out = edit_existing_data(id,label,value)
    return out
@app.post("/delete_existing")
def delete_existing():
    data = request.get_json()
    id = data["_id"]
    out = delete_existing_data(id)
    return out




