word=input("Enter a string:")
upcount,lowcount=0,0
for ch in word:
   if ch>='A' and ch<='Z':
      upcount+=1
   elif ch>='a' and ch<='z':
      lowcount+=1
print("Lowercase count:",lowcount)
print("Uppercase count:",upcount)
