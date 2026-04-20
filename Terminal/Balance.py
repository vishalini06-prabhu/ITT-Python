bal=int(input("Enter your account balance:"))
amt=int(input("Enter your amount to withdraw:"))
if(bal>=amt and amt%100==0):
    bal-=amt
    print("Rs. ",amt," Withdrawn successfully")
else:
  print("Cannot withdraw amount")  
print("Balance: Rs.",bal)
