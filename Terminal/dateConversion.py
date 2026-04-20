def date_conversion_problem():
    T = int(input("Enter total units (weeks + days) T: "))
    D_total = int(input("Enter total number of days D_total: "))

    # Check constraints
    if D_total < 7:
        print("INVALID INPUT: D_total must be at least 7.")
        return
    if T >= D_total:
        print("INVALID INPUT: T must be less than D_total.")
        return

    # Try possible values for days D from 0 to T
    for D in range(T + 1):
        W = T - D  # weeks
        # Total days = 7*W + D
        total_days = 7 * W + D
        if total_days == D_total:
            print(f"W = {W}, D = {D}")
            return

    print("INVALID INPUT")

print("\n Date Conversion Problem")
date_conversion_problem()
