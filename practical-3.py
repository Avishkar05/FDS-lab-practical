"""
ASSIGNMENT NO-03
PROGRAM TO IMPLEMENT MATRIX OPERATION USING ARRAY
Name :- Avishkar Haridas Zende
Roll no. :-73
"""
m=int(input("Enter no. of rows of matrix : "))
n=int(input("Enter no. of columns of matrix : "))
print("Enter the values into matrix1::")
matrix1=[[int(input())for i in range(m)]for j in range (n)]
print("Matrix 1 is")
for i in range(m):
for j in range(n):
print(matrix1[i][j],end=" ")
print()
print("Enter the values into matrix2::")
matrix2=[[int(input())for i in range(m)]for j in range (n)]
print("Matrix 2 is")
for i in range(m):
for j in range(n):
print(matrix2[i][j],end=" ")
print()
result1=[[0 for i in range(m)]for j in range (n)]
print("Addition Result ")
for i in range(m):
for j in range(n):
result1[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range (m):
for j in range (n):
print(result1[i][j],end=" ")
print()
result2=[[0 for i in range(m)]for j in range (n)]
print("Substraction Result ")
for i in range(m):
for j in range(n):
result2[i][j]=matrix1[i][j]-matrix2[i][j]
for i in range (m):
for j in range (n):
print(result2[i][j],end=" ")
print()
result3=[[0 for i in range(m)]for j in range (n)]
print("Transpose Matrix Result ")
for i in range(m):
for j in range(n):
result3[j][i]=matrix1[i][j]
for i in range (m):
for j in range (n):
print(result3[i][j],end=" ")
print()
result4=[[0 for i in range(m)]for j in range (n)]
print("Multiplication is ")
for i in range(m):
for j in range(n):
for k in range(m):
result4[i][j]=result4[i][j]+matrix1[i][k]*matrix2[k][j]
for i in range (m)
for j in range (n):
print(result4[i][j],end=" ")
print()
"""
**********************************OUTPUT*******************************************
Enter no. of rows of matrix : 4
Enter no. of columns of matrix : 4
Enter the values into matrix1::
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
Matrix 1 is
1 2 3 4
5 6 7 8
9 1 2 3
4 5 6 7
Enter the values into matrix2::
9
8
7
6
5
4
3
2
1
9
8
7
6
5
4
3
Matrix 2 is
9 8 7 6
5 4 3 2
1 9 8 7
6 5 4 3
Addition Result
10 10 10 10
10 10 10 10
10 10 10 10
10 10 10 10
Substraction Result
-8 -6 -4 -2
0 2 4 6
8 -8 -6 -4
-2 0 2 4
Transpose Matrix Result
1 5 9 4
2 6 1 5
3 7 2 6
4 8 3 7
Multiplication is
46 63 53 43
130 167 141 115
106 109 94 79
109 141 119 97
"""
