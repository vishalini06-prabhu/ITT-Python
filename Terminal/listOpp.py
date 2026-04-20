print("1.Second largest element")
print("2.Find products of list elements")
print("3.Find the element with given frequency:")
print("4.Exit")
l1=list(eval(input("Enter the list elements:")))
l2=[]
ele=[]
pro=1
while(True):
    choice=int(input("Enter your choice:"))
    if choice==1:
        for i in l1:
            if i not in l2:
                l2.append(i)
        l2.sort(reverse = True)
        print("Second largest element is:",l2[1])
    elif choice==2:
        for i in l1:
            pro*=i
        print("Products of elements:",pro)
        pro=1
    elif choice==3:
        fre=int(input("Enter the frequency  :"))
        for i in l1:
                  if l1.count(i)==fre:
                            if i not in ele:
                                      ele.append(i)
        print("element is",ele)
    elif choice == 4:
        print("exiting...")
        break
    else:
        print("Enter valid choice")
