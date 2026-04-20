unit=int(input("Enter a number of units:"))
if unit<=100:
   print("No amount")
elif unit>100 and unit<=200:
   price=(unit-100)*5
   print("Amount to be paid is",price)
else:
   price=500+(unit-200)*10
   print("Amount to be paid is",price)
