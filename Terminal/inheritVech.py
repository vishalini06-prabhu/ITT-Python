class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}, Year: {self.year}") 
class Car(Vehicle):
    def __init__(self, make, year, fuel_type):
        super().__init__(make, year)
        self.fuel_type = fuel_type
    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}") 
class Bike(Vehicle):
    def __init__(self, make, year, bike_type):
        super().__init__(make, year)
        self.bike_type = bike_type
    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.bike_type}")

print("Enter details for Car:") 
car_make = input("Make: ") 
car_year = int(input("Year: ")) 
car_fuel_type = input("Fuel Type (Petrol/Diesel/Electric): ") 
car = Car(car_make, car_year, car_fuel_type) 
print("\nEnter details for Bike:") 
bike_make = input("Make: ") 
bike_year = int(input("Year: ")) 
bike_type = input("Type of Bike (Cruiser/Sport/Standard/etc.): ") 
bike = Bike(bike_make, bike_year, bike_type) 
print("\nCar Information:") 
car.display_info() 
print("\nBike Information:") 
bike.display_info()
