import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
A = set(map(int,input().strip().split()))
B = set(map(int, input().strip().split()))
C = A-B
D = B-A
print(len(C)+len(D))