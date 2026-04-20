n=int(input("Enter a number(n):"))
sum=0
if(n<1 or n>100000):
    print("The value of n must be in the range 1<=n<=100000")
else:
    for i in range(1,n+1):
        if(i%2==0):
            sum+=1
    print("Number of even numbers between 1 and ",n," is ",sum)
