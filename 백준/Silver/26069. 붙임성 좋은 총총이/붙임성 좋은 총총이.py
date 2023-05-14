import sys
input = sys.stdin.readline

N=int(input())
A=["ChongChong"]
sum=0
for _ in range(N):
    human1,human2=input().strip().split()
    if human1 in A:
        A.append(human2)
    if human2 in A:
        A.append(human1)
print(len(set(A)))

