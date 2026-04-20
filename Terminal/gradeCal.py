mark=int(input("Enter your mark:"))
result = "Grade A" if mark >= 90 else "Grade B" if mark >= 75 else "Grade C" if mark>=60 else "Grade D"
print(result)
