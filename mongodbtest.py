import pymongo
import urllib.parse

#username = urllib.parse.quote_plus('harisreesa6')
#password = urllib.parse.quote_plus('Iris@gen360')
client = MongoClient(mongodb+srv://test:test360@cluster0.l0btmlv.mongodb.net/?retryWrites=true&w=majority)

db = client["test"]

def db_connect():
    #connecting to a DB in mongoDB
    try:
        if client.get_database("test"):
            print("Connection Successful!")
            return True
    except:
        print("Please check your connection")
        return False

def db_close():
    print ("Connection Getting Closed")
    client.close()

db_connect()
db_close()
