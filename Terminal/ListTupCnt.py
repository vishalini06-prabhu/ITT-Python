l=list(eval(input("Enter list elements:")))
count=0
print("Entered list:",l)
for i in l:
   if type(i)==tuple:
      break
   else:
      count+=1
print("Count:",count)
