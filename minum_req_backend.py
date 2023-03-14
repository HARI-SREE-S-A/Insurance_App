import time
from datetime import date,datetime
import sqlite3
l = []
database = sqlite3.connect("test databse")
cursor = database.cursor()

id = int(input("id"))
name = str(input("name"))
v_number = str(input("vehicle_number"))
ph = int(input("ph_n"))
company = str(input("insurance provider"))
amount = float(input("amount"))
date = (input("date"))
table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,customer_name TEXT,vehicle_number TEXT,phone_number 
INTEGER,insurance_provider_company TEXT,premium_amount INTEGER,Date TEXT);'''
cursor.execute(table)

table_data = '''INSERT INTO notes(id,customer_name,vehicle_number,phone_number,insurance_provider_company,
premium_amount,Date) VALUES(?,?,?,?,?,?,?)'''
cursor.execute(table_data, (id, name, v_number, ph, company, amount, date))
database.commit()
cursor.execute("SELECT * from notes;")
res = list(cursor.fetchall())
for n in range(len(res)):
    l.append(res[n][6])
print(l)

for o,i in enumerate(l):
    policy_exp = datetime = (datetime.strptime(i, '%d,%m,%Y'))
    ExpirationDate = time.strftime("%d,%m,%Y")
    T_date = (datetime.strptime(ExpirationDate, '%d,%m,%Y'))
    Req_d = policy_exp-T_date

    if Req_d.days < 10:
        print(Req_d)
        print(res[o][1],res[o][3],i)

cursor.close()
database.close()

