N =int(input("Enter a number:"))
total = 0
while N > 0:
    digit=N%10
    total+=digit
    N = N // 10
print("Sum of digits is",total)
