import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [0 for _ in range(N)]
for _ in range(M):
    i,j,k=map(int,input().split())
    for t in range(i-1,j):
        A[t]=k
print(*A)