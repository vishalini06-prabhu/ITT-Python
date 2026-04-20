# Mock database with 3 employees
employee_db = {
    "E001": {"name": "Vish", "role": "Manager", "salary": 80000},
    "E002": {"name": "Shalu", "role": "Developer", "salary": 60000},
    "E003": {"name": "Lini", "role": "Developer", "salary": 55000},
}
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_bonus(self):
        return 0
    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}") 
class Manager(Employee):
    def calculate_bonus(self):
        bonus_percentage = 10 # Fixed at 10%
        return self.salary * (bonus_percentage / 100) 
class Developer(Employee):
    def calculate_bonus(self):
        bonus_percentage = 7.5 # Fixed at 7.5%
        return self.salary * (bonus_percentage / 100)

emp_id = input("Enter your Employee ID: ").strip().upper() 
if emp_id in employee_db:
    record = employee_db[emp_id]
    name = record["name"]
    role = record["role"]
    salary = record["salary"]
    if role == "Manager":
        employee = Manager(name, salary)
    elif role == "Developer":
        employee = Developer(name, salary)
    else:
        print("Unknown role. Cannot calculate bonus.")
        exit()
    print("\nEmployee Details:")
    employee.display_info()
    bonus = employee.calculate_bonus()
    print(f"Fixed Bonus: {bonus:.2f}")
else:
    print("Employee ID not found.")
