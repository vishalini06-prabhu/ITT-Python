sal=int(input("Enter your salary:"))
print("-----------COMPUTED TAX-----------")
if sal<=250000:
    print("Salary: Rs. ",sal)
    print("No tax")
elif sal>250000 and sal<=500000:
    tax=sal*0.05
    print("5% TAX")
    print("Salary: Rs. ",sal)
    print("Tax amount Rs.",tax)
elif sal>500000 and sal<=1000000:
    tax=sal*0.1
    print("10% TAX")
    print("Salary: Rs. ",sal)
    print("Tax amount Rs.",tax)
else:
    tax=sal*0.15
    print("15% TAX")
    print("Salary: Rs. ",sal)
    print("Tax amount Rs.",tax)

