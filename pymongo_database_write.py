from pymongo import MongoClient



def db_connect():
    try:
        client = pymongo.MongoClient(connection_s)
        print("perfect")
    except Exception:
        print("failed connection" + Exception)
def database_update():
    name = str(input("name"))
    address = str(input("address"))
    ph = int(input("phone"))
    vehicle_number = str(input("vehicle number"))
    Date = str(input("dd,mm,yyyy"))

    mydb = client["Insuarance_app"]
    mycollections = mydb["customer_data"]
    mydocument = {
        "name": name,
        "ph": ph,
        "address":address,
        "vehicle_number":vehicle_number,
        "Date":Date
        
    }
    return mycollections

def database_res():
    res = mycollections.insert_one(mydocument)
    print(res.inserted_id)
    print(client.list_database_names())
