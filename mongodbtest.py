import pymongo
import urllib.parse

username = urllib.parse.quote_plus('harisreesa6')
password = urllib.parse.quote_plus('Iris@gen360')
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

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
