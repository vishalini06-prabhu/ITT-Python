mat=int(input("Enter maths mark:"))
sci=int(input("Enter science mark:"))
eng=int(input("Enter english mark:"))
if((1>mat or mat>100) or (1>sci or sci>100) or (1>eng or eng>100)):
    print("Enter according to the given constrains  0 <= marks <= 100")
else:
    sum=mat+sci+eng
    print("Sum is",sum)
    print("Average=",(sum/3))
