import sys
input = sys.stdin.readline

T = int(input())
A = list(map(int,input().strip().split()))
v = int(input())
count=0
for i in A:
    if i == v:
        count+=1
print(count)
