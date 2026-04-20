s=input("Enter a sentence:")
sent=s.split()
l1=[]
for ch in sent:
   if ch not in l1:
      l1.append(ch)
   else:
      print("First repeated word is ",ch)
      print("Index:",sent.index(ch)+1)
      break
