import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(M)]
C = list(set(A) & set(B))
C.sort()
print(len(C))
for i in C:
    print(i)