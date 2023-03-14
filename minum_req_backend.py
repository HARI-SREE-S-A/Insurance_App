mport sqlite3
import time
from datetime import date, datetime

database = sqlite3.connect("insurance_db")
cur = database.cursor()


def create_data():
    id = int(input("id"))
    name = str(input("name"))
    v_number = str(input("vehicle_number"))
    ph = int(input("ph_n"))
    company = str(input("insurance provider"))
    amount = float(input("amount"))
    date = (input("date"))
    table = '''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,customer_name TEXT,vehicle_number TEXT,phone_number 
    INTEGER,insurance_provider_company TEXT,premium_amount INTEGER,Date TEXT);'''
    cur.execute(table)

    table_data = '''INSERT INTO notes(id,customer_name,vehicle_number,phone_number,insurance_provider_company,
    premium_amount,Date) VALUES(?,?,?,?,?,?,?)'''
    cur.execute(table_data, (id, name, v_number, ph, company, amount, date))
    database.commit()


def view_databse():
    cur.execute("SELECT * from notes;")
    res = list(cur.fetchall())
    print(res)


def expiring(k):
    l = []
    dictn = {}
    cur.execute("SELECT * from notes;")
    res = list(cur.fetchall())
    for n in range(len(res)):
        l.append(res[n][6])
        for o, i in enumerate(l):
            policy_exp = (datetime.strptime(i, '%d,%m,%Y'))
            ExpirationDate = time.strftime("%d,%m,%Y")
            T_date = (datetime.strptime(ExpirationDate, '%d,%m,%Y'))
            Req_d = policy_exp - T_date

            if Req_d.days < k:
                dictn[Req_d.days] = (res[o][1], res[o][3], i)
                # print(res[o][1],res[o][3],i)

    print(dictn)


#create_data()
#view_databse()
expiring(int(input("short listing days")))


cur.close()

database.close()
