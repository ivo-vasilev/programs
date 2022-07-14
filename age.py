import datetime
import humanize


today = datetime.datetime.now()

name = str(input("Name: ").strip().title())

while True:
    try:
        year = int(input("Year: "))
    except ValueError:
        print("Input year with numbers only!")
    else:
        break

while True:
    try:
        month = int(input("Month: "))
    except ValueError:
        print("Input month with numbers only!")
    else:
        break

while True:
    try:
        day = int(input("Day: "))
    except ValueError:
        print("Input day with numbers only!")
    else:
        break

bday = datetime.datetime(year, month, day)

print(f"{name} was born " + humanize.naturaltime(today - bday))
