def fibbo(n):
    if n==1 or n==0:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)
ran=int(input("Enter the number of terms:"))
print("Fibonacci Series:")
for i in range(ran):
    print(fibbo(i),end=" ")
