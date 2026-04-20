n=input("Enter a string:")
l=[]
for x in n:
   if x not in l:
      l.append(x)
a=" ".join(l)
print(a)
