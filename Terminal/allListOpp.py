print("List opperations")
print("1.append")
print("2.insert")
print("3.remove")
print("4.pop")
print("5.extend")
print("6.exit")
while (True):
    choice=int(input("Enter your choice:"))
    if  choice==1:
        l1=list(eval(input("Enter the list elements:")))
        print("List before appending:",l1)
        ele=input("Enter element to append:")
        if ele.isdigit():
            ele=int(ele)
        l1.append(ele)
        print("List after appending:",l1)
    elif choice==2:
        l1=list(eval(input("Enter the list elements:")))
        print("List before inserting:",l1)
        ele=input("Enter element to insert:")
        if ele.isdigit():
            ele=int(ele)
        index=int(input("Enter index to be inserted at:"))
        l1.insert(index-1,ele)
        print("List after inserting:",l1)
    elif choice ==3:
        l1=list(eval(input("Enter the list elements:")))
        print("List before removing:",l1)
        ele=input("Enter element to remove:")
        if ele.isdigit():
            ele=int(ele)
        l1.remove(ele)
        print("List after removing:",l1)
    elif choice ==4:
        l1=list(eval(input("Enter the list elements:")))
        print("List before poping:",l1)
        l1.pop()
        print("List after poping:",l1)
    elif choice ==5:
         l1=list(eval(input("Enter the list1 elements:")))
         l2=list(eval(input("Enter the list2 elements:")))
         print("l1=",l1)
         print("l1=",l2)
         l1.extend(l2)
         print("List1 after extending:",l1)
    elif choice ==6:
           print("Exiting...")
           break
    else:
               print("Invalid input")
