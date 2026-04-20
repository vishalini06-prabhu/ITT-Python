try:
    # 1. Ask for input with a clear prompt
    print("Enter two integers separated by a space (e.g., 10 2):")
    raw_data = input().split()

    # 2. Check if the user actually gave two values
    if len(raw_data) != 2:
        # This manually triggers the "Invalid input" block below
        raise ValueError 

    # 3. Try to convert the strings to integers
    a = int(raw_data[0])
    b = int(raw_data[1])

    # 4. Perform the division
    result = a / b
    print("The result is:")
    print(result)

except ZeroDivisionError:
    # Triggers if the second number is 0
    print("Error: Division by zero")

except ValueError:
    # Triggers if input is a letter, a decimal, or missing a number
    print("Error: Invalid input")
