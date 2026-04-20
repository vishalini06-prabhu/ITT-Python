import math
print("Available Mathematical Operations Using 'math' Module:\n")

# Basic Mathematical Operations
num = float(input("Enter a number: "))

print(f"\nSquare root of {math.fabs(num)}: {math.sqrt(math.fabs(num))}")
print(f"Absolute value of {num}: {math.fabs(num)}")
print(f"Ceiling value of {num}: {math.ceil(num)}")
print(f"Floor value of {num}: {math.floor(num)}")
print(f"Power {num}^2: {math.pow((num), 2)}")
print(f"Exponential of {num}: {math.exp(num)}")

#Converting degree to radians
angle = float(input("\nEnter an angle in degrees: "))
radians = math.radians(angle) 
print(f"{angle} in radians: {radians}")

# Constant
print(f"\nValue of pi: {math.pi}")

# GCD (Greatest Common Divisor)
a = int(input("\nEnter first integer for GCD: "))
b = int(input("Enter second integer for GCD: "))
print(f"GCD of {a} and {b}: {math.gcd(a, b)}")

print("\nAll operations performed successfully!")

