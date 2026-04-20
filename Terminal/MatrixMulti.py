rows1=int(input("Enter the number of rows of matrix 1:"))
cols1=int(input("Enter the number of columns of matrix 1:"))
rows2=int(input("Enter the number of rows of matrix 2:"))
cols2=int(input("Enter the number of columns of matrix 2:"))
t,m1,m2,=[],[],[]
res = [[0] * cols2 for _ in range(rows1)]
if cols1!=rows2:
          print("First matix column and the second matrix rows should have same dimension for matrix multiplication")
else:
          print("MATRIX 1")
          for i in range(rows1):
                    t=[]
                    for j in range(cols1):
                              val=int(input(f"Enter the element m1[{i+1}][{j+1}]:"))
                              t.append(val)
                    m1.append(t)
          print("MATRIX 2")
          for i in range(rows2):
                    t=[]
                    for j in range(cols2):
                              val=int(input(f"Enter the element m2[{i+1}][{j+1}]:"))
                              t.append(val)
                    m2.append(t)
          for i in range(rows1):
                    for j in range(cols2):
                              for k in range(cols2):
                                        res[i][j]+=m1[i][k]*m2[k][j]
          print("Matrix 1:", m1)
          print("Matrix 2:", m2)
          print("Resultant Matrix:")
          for row in res:
                    print(row)
