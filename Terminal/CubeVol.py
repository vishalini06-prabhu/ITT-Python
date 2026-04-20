s=int(input("Enter length of cube:"))

if((1>s or s>50)):
    print("Enter according to the given constrains  1 <= side <= 50")

else:
    vol=s*s*s
    print("Volume of cube is",vol)
