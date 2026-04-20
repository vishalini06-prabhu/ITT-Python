num = int(input("Enter number of cases: "))
R = num
mat = []

print("Enter values row-wise:")
for i in range(R):
    row = list(map(str, input().split('.')))
    mat.append(row)
i = 0
while i < num:
    no1 = mat[i][0]
    no2 = mat[i][1]
    no3 = mat[i][2]
    no4 = mat[i][3]
    ch='$%^&*'
    if (no1.isalpha() or no2.isalpha or no3.isalpha() or no4.isalpha()):
         print("INVALID")
         break
    elif ((no1 in ch) or (no2 in ch) or (no3 in ch) or (no4 in ch)):
        print("INVALID")
    elif (int(no1)>=256 or int(no2)>=256 or int(no3)>=256 or int(no4)>=256):
        print("INVALID")
    else:
        print("VALID")
    i=i+1
