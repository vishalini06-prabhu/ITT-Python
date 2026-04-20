sent=input("Enter a word :")
l1=[]
count=[]
i,ct=0,0
for ch in sent:
   if ch not in l1:
      l1.append(ch)
for i in l1:
   for ch in sent:
      if ch == i:
         ct=ct+1
   count.append(ct)
   ct=0
for ch in range(len(l1)):
   print(l1[ch],count[ch])
