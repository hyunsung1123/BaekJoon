import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [i for i in range(1,N+1)]
for i in range(M):
    i,j = map(int,input().split())
    A[i-1:j] = reversed(A[i-1:j])
print(*A)