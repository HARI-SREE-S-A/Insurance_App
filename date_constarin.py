import sqlite3
import time
from dateutil import parser
from datetime import date, datetime

l = []

databse = [(0, 'test0', 'kl001234a', 1234567890, 'hdfc', 1223.33, '15,03,2023'),
           (1, 'test01', 'kl22as1234', 1234567890, 'hdfc', 1234.44, '22,05,2023'),
           (2, 'test2', 'kl99zx1234', 1234567890, 'ybgf', 2222.33, '16,01,2023'),
           (3, 'test3', 'kl00ax1234', 1234567890, 'bbdf', 1111.11, '11,09,2023'),
           (4, 'test4', 'kl88aa1234', 1234567890, 'bdfc', 2222.67, '10,04,2023'),
           (5, 'test5', 'kl00aa1234', 123456789, 'ghty', 222.55, '11,05,2023')]
for n in range(len(databse)):
   l.append(databse[n][6])
   x = 0
for i in l:
    datet = (i)
    x +=1

    # print(time.strftime("%d-%m-%Y"))
    # print(datet)

    ExpirationDate = time.strftime("%d,%m,%Y")
    T_date = (datetime.strptime(ExpirationDate,'%d,%m,%Y'))
    datetime = (datetime.strptime(i, '%d,%m,%Y'))

    print((T_date), i,x)



    d = datetime
    a = d
    b = T_date
    delta = a - b

    print(delta)

    if delta.days < 30:
        print( "alert")
    else:
        print("License OK")

