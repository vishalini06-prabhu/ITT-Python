def calculate_days_hours():
    # Get inputs from user
    T = int(input("Enter total units (days + extra hours) T: "))
    H_total = int(input("Enter total hours H_total: "))

    # Check input constraints
    if H_total < 24:
        print("INVALID INPUT: H_total must be at least 24.")
        return
    if H_total % 2 != 0:
        print("INVALID INPUT: H_total must be an even number.")
        return
    if T >= H_total:
        print("INVALID INPUT: T must be less than H_total.")
        return

    # Try possible values for extra hour units H
    for H in range(0, T + 1):
        D = T - H  # full days
        if H == 0:
            # When no extra hours, check if total hours = 24 * D
            if 24 * D == H_total:
                print(f"D = {D}, H = {H}")
                return
            else:
                continue

        # Calculate X = hours per extra hour unit
        numerator = H_total - 24 * D
        if numerator % H == 0:
            X = numerator // H
            if X > 0:
                print(f"D = {D}, H = {H}")
                return

    # If no solution found
    print("INVALID INPUT")

# Run the function
calculate_days_hours()
