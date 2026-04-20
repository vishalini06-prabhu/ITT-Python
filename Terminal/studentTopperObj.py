class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

students = [
    Student("Alice", 101, [90, 85, 88]),
    Student("Bob", 102, [78, 80, 74]),
    Student("Vish", 103, [95, 92, 90]),
]

topper = max(students, key=lambda s: s.total_marks())

print(f"Topper: {topper.name} \nRoll No: {topper.roll_no}")
print(f"Total Marks: {topper.total_marks()}\nAverage: {topper.average_marks():.2f}")

