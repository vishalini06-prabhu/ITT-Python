class Vehicle:
    def __init__(self,brand,model,year,milage,vno):
        self.brand=brand
        self.model=model
        self.year=year
        self.mile=milage
        self.vno=vno
    def display(self):
        print(f'Vehilce number : {self.vno}')
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
        print(f"Milage : {self.mile}")
        print("--------------------------")
l=[]
n=int(input("Enter number of Vechicles:"))
for i in range(n):
    vno=i+1
    print(f"Vehicle {vno}:")
    brand=input("Enter brand name:")
    model=input("Enter your vehicle model:")
    year=int(input("Enter year of manufacture:"))
    mil=int(input("Enter vehicle milage:"))
    l.append(Vehicle(brand,model,year,mil,vno))
for i in l:
    i.display()
