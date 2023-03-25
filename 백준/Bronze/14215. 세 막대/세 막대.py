A=list(map(int,input().split(" ")))
A.sort()
print(A[0]+A[1]+min(A[2],(A[0]+A[1]-1)))

