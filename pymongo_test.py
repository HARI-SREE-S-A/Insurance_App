mport pymongo

connection_s = "mongodb+srv://test:test360@cluster0.l0btmlv.mongodb.net/?retryWrites=true)"
try:
    client = pymongo.MongoClient(connection_s)
    print("perfect")
except Exception:
    print("failed connection" + Exception)

mydb = client["test_db"]

mycollections = mydb["test_collection"]

mydocument = {
    "name": "test0",
    "ph": "1234567890"
}

res = mycollections.insert_one(mydocument)
print(res.inserted_id)

print(client.list_database_names())

