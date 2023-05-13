import sys
input = sys.stdin.readline


T=int(input())
A =list(map(int,input().strip().split()))
A.sort()
print(A[0]*A[-1])
