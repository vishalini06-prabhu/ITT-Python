pur1=int(input("Enter your purchase amount:"))
result = (pur1*(0.2)) if pur1>=5000 else (pur1*(0.1)) if pur1>=3000 else "No discount"
print("----------------Raha Store------------------")
print("22,Ghandi street,Mumbai,629034")
print("mobile no:9983748657")
print("---------------------BILL------------------")
print("Oder id:98973H")
print("Purchase Amount: Rs.",pur1)
res= print("Deduced Amount: Rs.",result) if pur1>=5000 else print("Deduced Amount: Rs.",result) if pur1>=3000 else "No discount"
print("-------------------------------------------")
print("Total Amount to be Paid: Rs.",pur1-result)
print("-------------------------------------------")
