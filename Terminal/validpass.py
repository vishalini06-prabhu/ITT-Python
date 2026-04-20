hasup,haslow,hasdigi,hasch=0,0,0,0
for ch in password:
   if ch.isdigit():
      hasdigi=1
   if ch.islower():
      haslow=1
   if ch.isupper():
      hasup=1
spchr="@#$^&*"
for i in spchr:
   if i in password:
      hasch=1
if hasdigi==0:
   print("Invalid password due to abscence of digits")
if haslow==0:
   print("Invalid password.Password should contain atleast 1 lowercase character")
if hasup==0:
   print("Invalid password.Password should contain atleast 1 uppercase character")
if not 8<=len(password)<=15:
   print("Password length should be between 8 and 15")
if " " in password:
   print("Invalid password.It should not contain space")
if hasch==0:
   print("Invalid password as it should have special characters like",spchr)
if hasup==1 and haslow==1 and hasdigi==1 and hasch==1:
   print("Valid password")
