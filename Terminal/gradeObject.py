class Person:
    def __init__(self, name, age, gender, marks_obtained, total_marks):
        self.name = name
        self.age = age
        self.gender = gender
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks

    def calculate_percentage(self):
        return (self.marks_obtained / self.total_marks) * 100

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks Obtained: {self.marks_obtained}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")


person1 =Person("John", 20, "Male", 450, 500)
person2 =Person("Malu", 18, "Female", 470, 500)

person1.display_details()
person2.display_details()
