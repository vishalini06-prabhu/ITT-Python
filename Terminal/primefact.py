#Prime factor using recursion
def prime_factors(n,factor=2):
   if n<=1:
      return 1
   if n%factor==0:
      print(factor,end=" ")
      prime_factors(n//factor,factor)
   else:
      prime_factors(n,factor+1)
num=int(input("Enter a number:"))
print("Prime factors:",end=" ")
prime_factors(num)
