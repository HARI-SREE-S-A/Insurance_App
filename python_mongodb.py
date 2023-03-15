import pymongo


name = str(input("name"))
address = str(input("address"))
ph = int(input("phone"))
vehicle_number  = str(input("vehicle number"))
Date = str(input("dd,mm,yyyy")) 
# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database
mydb = client["Insurance_app"]

# Create a new collection (i.e. table)
mycol = mydb["customers_info"]

# Insert a document (i.e. row) into the collection
mydict = { "name": name, "address": address,"ph_number":ph,"vehicle_number":vehicle_number,"policy_expiry":Date}
x = mycol.insert_one(mydict)

# Print the ID of the inserted document
print(x.inserted_id)
