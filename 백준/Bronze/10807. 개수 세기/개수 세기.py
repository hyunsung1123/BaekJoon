import sys
input = sys.stdin.readline

T = int(input())
A = list(map(int,input().strip().split()))
v = int(input())
print(A.count(v))