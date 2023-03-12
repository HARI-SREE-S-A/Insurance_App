import pandas as pd
import sqlite3

jmnhhg
f

database = sqlite3.connect("test databse")
cursor = database.cursor()

id = int(input("id"))
name = str(input("name"))
v_number = str(input("vehicle_number"))
ph = int(input("ph_n"))
company = str(input("insurance provider"))
amount = float(input("amount"))
date = int(input("date"))
table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,customer_name TEXT,vehicle_number TEXT,phone_number 
INTEGER,insurance_provider_company TEXT,premium_amount INTEGER,Date TEXT);'''
cursor.execute(table)


table_data = '''INSERT INTO notes(id,customer_name,vehicle_number,phone_number,insurance_provider_company,
premium_amount,Date) VALUES(?,?,?,?,?,?,?)'''
cursor.execute(table_data,(id,name,v_number,ph,company,amount,date))
database.commit()
cursor.execute("SELECT * from notes;")
res = cursor.fetchall()
print(res)
cursor.close()
database.close()
