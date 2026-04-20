s={}
nd=int(input("Enter number of student: "))
for _ in range(nd):
       name=input("Enter student name:")
       n=int(input("Enter the  mark: "))
       if n>=90:
           print("Your grade is O")
       elif n>=80 and n<89:
           print("Your grade is A+")
       elif n>=70 and n<79:
           print("Your grade is A")
       elif n>=60 and n<69:
           print("Your grade is B+")
       elif n>=55 and n<59:
           print("Your grade is B")
       elif n>=50 and n>=54:
           print("your grade is c")
       else:
           print("You are Fail") 
       s[name]=n
print("\n Student grade")
for u in s.keys():
    print(f"{u}:{s.get(u)}")
