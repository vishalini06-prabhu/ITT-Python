a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
res=a if a>b and a>c else b if b>c else c
print("Largest number : ",res)
