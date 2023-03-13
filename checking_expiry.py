import sqlite3
import time
l = []




databse = [(0, 'test0', 'kl001234a', 1234567890, 'hdfc', 1223.33, '13-02-2023'), (1, 'test01', 'kl22as1234', 1234567890, 'hdfc', 1234.44, '12-03-2023'), (2, 'test2', 'kl99zx1234', 1234567890, 'ybgf', 2222.33, '15-04-2023'), (3, 'test3', 'kl00ax1234', 1234567890, 'bbdf', 1111.11, '12-11-2023'), (4, 'test4', 'kl88aa1234', 1234567890, 'bdfc', 2222.67, '12-04-2023'), (5, 'test5', 'kl00aa1234', 123456789, 'ghty', 222.55, '12-05-2023')]
for n in range(len(databse)):
    l.append(databse[n][6])
for i in l:
    datet = i

    print (time.strftime("%d-%m-%Y"))
    print(datet)



    class Timedelta(object):
        @property
        def isoformat(self):
               return str()

    ExpirationDate = time.strftime("%d-%m-%Y")
    if ExpirationDate >= datet:
        print('Renew License Soon')
    elif ExpirationDate == datet:
        print('Renew License Immediately')
    else:
        print("License OK")
