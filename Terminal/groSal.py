sal=int(input("Enter Basic Salary:"))
da=0.20*sal
hra=0.10*sal
if((5000>sal or sal>50000)):
    print("Enter according to the given constrains  5000 <= salary <= 50000")

else:
    gro=sal+da+hra
    print("Gross Salary is",gro)
