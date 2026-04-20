def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    return a/b
choice="y"
print("     Opperations")
print("1.Adittion\n2.Subtraction\n3.Multiplication\n4.Division")
while(choice =="y"):
    n1,n2=[int(i) for i in input("Enter two numbers:").split()]
    opp=input("Enter opperator(+,-,*,/):")
    if opp == '+':
        s=add(n1,n2)
        print("Addition=",s)
        choice=input("Do you want to continue (y/n):")
    elif opp == '-':
        diff=sub(n1,n2)
        print("Difference=",diff)
        choice=input("Do you want to continue (y/n):")
    elif opp == '*':
        pro=mul(n1,n2)
        print("Product=",pro)
        choice=input("Do you want to continue (y/n):")
    elif opp == "/":
        div=division(n1,n2)
        print("Quotient= %.2f" %div)
        choice=input("Do you want to continue (y/n):")
    else:
        print("Enter a valid choice")
else:
    print("Exiting...")
    exit()
