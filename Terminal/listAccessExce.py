try:
    # 1. Ask for the list of integers
    print("Enter list of integers (space separated):")
    # Convert input string into a list of integers
    numbers = list(map(int, input().split()))

    # 2. Ask for the index to access
    print("Enter the index you want to access:")
    index = int(input().strip())

    # 3. Try to access and print the element
    result = numbers[index]
    print("Element at index", index, "is:")
    print(result)

except IndexError:
    # Triggers if the index is too high (e.g., index 5 for a list of 4 items)
    print("Error: Index out of range")

except ValueError:
    # Triggers if the user types a letter, a decimal, or leaves it blank
    print("Error: Invalid input")
