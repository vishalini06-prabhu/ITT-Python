vow="aeiou"
wrd=input("Enter a sentence:")
lcwrd=wrd.lower()
vc,conc=0,0
for ch in lcwrd:
   if ch in vow:
      vc=vc+1
   else:
      if ch.isalpha():
         conc+=1
print("Vowel count:",vc)
print("Consonant count:",conc)
