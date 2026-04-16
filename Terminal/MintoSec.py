m=int(input("Enter minutes:"))

if((0>m or m>1000)):
    print("Enter according to the given constrains  0 <= min <= 1000")

else:
    sec=m*60
    print(m,"Minutes is",sec)
