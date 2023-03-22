import sys
A=[]
bigNumber =0
row,column = 0, 0
for i in range(9):
    i = list(map(int,sys.stdin.readline().split(" ")))
    A.append(i)
for i in range(9):
    for j in range(9):
        if A[i][j] >= bigNumber:
            row=i+1
            column=j+1
            bigNumber = A[i][j]
print(bigNumber)
print(row,column)
