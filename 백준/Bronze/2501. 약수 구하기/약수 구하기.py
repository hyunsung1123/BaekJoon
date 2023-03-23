N,K=map(int,input().split(" "))
A=[]
for i in range(1,N+1):
    if N%i ==0:
        A.append(i)
if len(A) < K:
    print(0)
else:
    print(A[K-1])