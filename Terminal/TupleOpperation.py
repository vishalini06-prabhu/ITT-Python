print("Tuple opperations")
print("1.count")
print("2.sort")
print("3.multiplication")
print("4.min")
print("5.max")
print("6.exit")
t=tuple(eval(input("Enter tuple elements:")))
while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Entered tuple:",t)
        ele=input("Element to be counted:")
        if ele.isdigit():
            ele=int(ele)
        if t.count(ele)==0:
            print("Element not found")
        else:
             print("Count of ",ele,"is:",t.count(ele))
    elif choice == 2:
        print("Entered tuple:",t)  
        t1=sorted(t)
        print("Tuple after sorting is",t1)
    elif choice ==3:
        print("Entered tuple:",t)  
        mul=int(input("Enter number of times to be multiplied:"))
        t2=t*mul
        print("Multiplied tuple:",t2)
    elif choice==4:
        print("Entered tuple:",t)
        print("Maximum element:",max(t))
    elif choice ==5:
        print("Entered tuple:",t)
        print("Minimum element:",min(t))
    elif choice ==6:
        print("Exitting...")
        break
    else:
        print("Invalid choice")
