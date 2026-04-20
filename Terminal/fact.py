n=int(input("Enter a number(n):"))
fact=1
if(n<1 or n>12):
    print("The value of n must be in the range 1<=n<=12")
else:
    for i in range(1,n+1):
        fact*=i
    print("Factorial of ",n," is ",fact)
