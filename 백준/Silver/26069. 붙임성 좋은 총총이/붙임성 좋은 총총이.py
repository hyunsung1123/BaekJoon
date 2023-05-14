import sys
input = sys.stdin.readline

N=int(input())
A=set()
A.add("ChongChong")
sum=0
for _ in range(N):
    human1,human2=input().strip().split()
    if human1 in A:
        A.add(human2)
    if human2 in A:
        A.add(human1)
print(len(A))


