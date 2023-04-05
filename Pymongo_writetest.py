from pymongo import MongoClient
import pymongo
connection_s = "mongodb+srv://test:harvis360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority"


def db_connect(connection_s):
    try:
        client= pymongo.MongoClient(connection_s)
        print("perfect")
    except Exception as e:
        print("failed connection" + str(e))
def database_update():
    client = pymongo.MongoClient(connection_s)

    name = str(input("name"))
    address = str(input("address"))
    ph = int(input("phone"))
    vehicle_number = str(input("vehicle number"))
    Date = str(input("yyyy,mm,dd"))

    mydb = client["Insuarance_app"]
    mycollections = mydb["customer_data"]
    mydocument = {
        "name": name,
        "ph": ph,
        "address":address,
        "vehicle_number":vehicle_number,
        "Date":Date

    }
    return mycollections,mydocument

def database_res(mycollections,mydocument):
    client = pymongo.MongoClient(connection_s)
    res = mycollections.insert_one(mydocument)
    print(res.inserted_id)
    print(client.list_database_names())

db_connect(connection_s)
colltn,document= database_update()

database_res(colltn,document)
