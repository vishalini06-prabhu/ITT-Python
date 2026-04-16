a=int(input("Enter value of celcius:"))

if(-50>a or a>100):
    print("The value of celcius must be between -50 and 100")
    a=int(input("Enter value of celcius:"))

print("Fahrenheit of",a," is",((a*1.8)+32))
