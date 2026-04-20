from datetime import datetime

# Note: Input format must be DD-MM-YYYY HH:MM:SS
print("Enter the first timestamp (DD-MM-YYYY HH:MM:SS):")
ts1_str = input().strip()

print("Enter the second timestamp (DD-MM-YYYY HH:MM:SS):")
ts2_str = input().strip()

# 2. Define the exact format matching the input
date_format = "%d-%m-%Y %H:%M:%S"

# 3. Convert the strings into datetime objects
t1 = datetime.strptime(ts1_str, date_format)
t2 = datetime.strptime(ts2_str, date_format)

# 4. Calculate the absolute difference in seconds
# (t2 - t1) creates a timedelta; .total_seconds() converts it to a number
difference_seconds = abs((t2 - t1).total_seconds())

# 5. Print the final result as an integer
print("The difference in seconds is:")
print(int(difference_seconds))
