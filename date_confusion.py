from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0



if delta.days > 10:
    print(delta.days)
