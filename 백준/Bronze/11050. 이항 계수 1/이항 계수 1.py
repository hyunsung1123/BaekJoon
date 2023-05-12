import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
A=1
temp=M
B=1
for i in range(M):
    A*=N
    N=N-1
for i in range(M):
    B*=temp
    temp-=1
print(A//B)