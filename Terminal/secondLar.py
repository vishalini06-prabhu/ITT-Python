a=int(input("Enter value of length:"))
b=int(input("Enter value of breadth:"))
if(a<1):
    print("The value of length greater than or equal to 1")
elif(b>100):
    print("The value of breadth must be less than or equal to 100")
else:
    print("Area of rectangle is",a*b)
