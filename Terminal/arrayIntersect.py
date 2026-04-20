def find_intersection(arr1,arr2):
   return list(filter(lambda x:x in arr2,arr1))
arr1=list(eval(input("Enter first array elements:")))
arr2=list(eval(input("Enter second array elements:")))
intersection=find_intersection(arr1,arr2)
if intersection==[]:
   print("No common elements")
else:
   print("Intersection of the two arrays:",intersection)
