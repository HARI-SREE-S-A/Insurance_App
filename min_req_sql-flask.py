from bson import ObjectId
from flask import Flask, request
import sqlite3
import time
from datetime import date, datetime
app = Flask(__name__)




def create_data(id,name,ph,amount,date):
    database = sqlite3.connect("insurance_db")
    cur = database.cursor()

    table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,customer_name TEXT,phone_number 
    INTEGER,premium_amount INTEGER,Date TEXT);'''
    cur.execute(table)

    table_data = '''INSERT INTO notes(id,customer_name,phone_number,premium_amount,Date) VALUES(?,?,?,?,?)'''
    cur.execute(table_data, (id, name, ph, amount, date))
    database.commit()
    return {"write":"success"}


@app.get("/viewall")
def get_store():
    database = sqlite3.connect("insurance_db")
    cur = database.cursor()
    cur.execute("SELECT * from notes;")
    res = (cur.fetchall())
    return res


@app.post("/create_data")
def test_update():
    data = request.get_json()
    print(data)
    id = data["id"]
    name = data["name"]
    ph = data["ph"]
    amount = data["amount"]
    date = data["date"]

    out  = create_data(id,name,ph,amount,date)

    return {"fetch":out}
