import sys
input = sys.stdin.readline
n,m= map(int,input().split(" "))
A = set([input() for _ in range(n)])
answer = 0
for i in range(m):
    a = input()
    if a in A:
        answer +=1
print(answer)