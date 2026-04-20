n=input("Enter String:")
opt=" "
for x in n:
   if x.isalpha():
      opt=opt+x
      prev=x
   else:
      opt=opt+prev*(int(x)-1)
print(opt)
