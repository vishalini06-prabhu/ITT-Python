rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the matrix row by row (only 0 and 1 are allowed):")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


is_binary = True  
for row in matrix:
    for num in row:
        if num not in [0, 1]:
            is_binary = False
            break

if not is_binary:
    print("Warning: The matrix is not binary!")
else:
    
    max_ones = 0
    row_number = -1
    current_row_index = 1

    for row in matrix:
        ones_count = row.count(1)  
        if ones_count > max_ones:  
            max_ones = ones_count
            row_number = current_row_index  
        current_row_index += 1 

    
    if row_number != -1:
        print(f"Row {row_number} contains the maximum number of 1's, which is {max_ones}.")
    else:
        print("No 1's found in the matrix.")
