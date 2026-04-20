class Account:
   def __init__(self,holder,AcNo,balance):
      self.holder=holder
      self.AcNo=AcNo
      self.balance=balance
   def showbalance(self):
      print(f"Holder name: {self.holder}")
      print(f"Account Number: {self.AcNo}")
      print(f"Balance: {self.balance}\n")
   def deposit(self,amount):
      self.balance+=int(amount)
      print(f"{amount} deposited successfully!")
class SavingsAccount(Account):
   def __init__(self,holder,AcNo,balance,rate):
      super().__init__(holder,AcNo,balance)
      self.rate=rate
   def CalculateInterest(self):
      time=1
      return (int(self.balance)*time*rate)/100
   def Showbalance(self):
      super().showbalance()
DB={'12345678910':{'name':'Ravi','bal':100000,'rate':10},
     '2345678689':{'name':'Raju','bal':200000,'rate':30},
     '8937493274':{'name':'Paru','bal':234567,'rate':40}
   }
acno=input("Enter your account number:")
amount=int(input("Amount to deposit:"))
if acno in DB:
   details=DB[acno]
   name=details['name']
   bal=details['bal']
   rate=details['rate']
   a1=Account(name,acno,bal)
   print("Your account Details:")
   a1.showbalance()
   a1.deposit(amount)
   print("Balance After deposit")
   a1.showbalance()
   a2=SavingsAccount(name,acno,a1.balance,rate)
   Interest=a2.CalculateInterest()
   print("Savings account details")
   print(f"Interest:{Interest}")
   a2.showbalance()
else:
   print("Invalid account number")
