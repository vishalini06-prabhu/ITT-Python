a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
choice=input("Enter a operand (+,-,*,/):")
match choice:
    case '+':
        sum=a+b
        print("Sum of " ,a, "and" ,b ,"=",sum)
    case '-':
        diff=a-b
        print("Difference of " ,a, "and" ,b, "=",diff)
    case '*':
        mul=a*b
        print("Product of ", a, "and" ,b ,"=",mul)
    case '/':
        div=a/b
        print("Quotient of " ,a, "and" ,b, "=",div)
    case _:
        print("Invalid operand")
