mport sqlite3
import time
from dateutil import parser
from datetime import date, datetime


l = []

databse = [(0, 'test0', 'kl001234a', 1234567890, 'hdfc', 1223.33, '02,13,2023'),
           (1, 'test01', 'kl22as1234', 1234567890, 'hdfc', 1234.44, '03,12,2023'),
           (2, 'test2', 'kl99zx1234', 1234567890, 'ybgf', 2222.33, '04,15,2023'),
           (3, 'test3', 'kl00ax1234', 1234567890, 'bbdf', 1111.11, '11,11,2023'),
           (4, 'test4', 'kl88aa1234', 1234567890, 'bdfc', 2222.67, '10,04,2023'),
           (5, 'test5', 'kl00aa1234', 123456789, 'ghty', 222.55, '11,05,2023')]
for n in range(len(databse)):
    l.append(databse[n][6])
for i in l:
    datet = i


    # print(time.strftime("%d-%m-%Y"))
    # print(datet)



    ExpirationDate = time.strftime("%m,%d,%Y")
    print(ExpirationDate)
    da = parser.parse(i)
    db = parser.parse(ExpirationDate)
    date_format = "%m/%d/%Y"
    a = datetime.strptime(i, date_format)
    b = datetime.strptime(ExpirationDate, date_format)
    diff = b - a
    print(diff)

    if diff < 30:
        print(diff, "yes")
    elif ExpirationDate == datet:
        print('Renew License Immediately')
    else:
        print("License OK")

