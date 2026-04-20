n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
cubes = [( num,num**3) for num in numbers]
cubes_tuple = tuple(cubes)
print("Tuple of numbers and their cubes:", cubes_tuple)
