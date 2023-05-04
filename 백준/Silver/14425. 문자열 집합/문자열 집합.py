import sys
input = sys.stdin.readline
n,m= map(int,input().split(" "))
A = []
B = []
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
answer =0

for i in B:
    if i in A:
        answer +=1
print(answer)