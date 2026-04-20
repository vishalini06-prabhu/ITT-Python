import datetime

# 1. Read input as three integers
print("Enter The date in the format of (DD MM YYYY)");
day, month, year = map(int, input().split())

# 2. Create a date object
date_obj = datetime.date(year, month, day)

# 3. Get the day name and convert it to UPPERCASE
print(date_obj.strftime("%A").upper())
