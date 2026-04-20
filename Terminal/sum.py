n=int(input("Enter a number(n):"))
sum=0
if(n<1 or n>100000):
    print("The value of n must be in the range 1<=n<=100000")
else:
    for i in range(n+1):
        sum+=i
    print("Sum of first",n," natural numbers is ",sum)
