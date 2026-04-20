import math

class AreaCalculator:
    def area(self, *args):
        if len(args) == 1:
            
            radius = args[0]
            return math.pi * radius * radius
        
        elif len(args) == 2:
            
            length, breadth = args
            return length * breadth
        
        elif len(args) == 3:
            
            base, height, _ = args
            return 0.5 * base * height
        
        else:
            return "Invalid number of arguments for area calculation."


calc = AreaCalculator()

r=int(input("Enter the radius of circle:"))
print(f"Area of Circle : {calc.area(r):.2f}")

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of Rectangle:" ,calc.area(l, b))

lt=int(input("Enter the length of Triangle:"))
h=int(input("Enter the height of Triangle:"))
print("Area of Triangle:", calc.area(lt, h, 0))
