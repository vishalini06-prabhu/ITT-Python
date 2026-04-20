num = int(input("Enter number of cases: "))
R = num
mat = []

print("Enter values row-wise:")
for i in range(R):
    row = list(map(int, input().split()))
    mat.append(row)
i = 0
while i < num:
    no1 = mat[i][0]
    no2 = mat[i][1]
    if(no1<no2):
        print("FIRST")
    elif (no2<no1):
        print("SECOND")
    else:
        print("ANY")
    i=i+1
