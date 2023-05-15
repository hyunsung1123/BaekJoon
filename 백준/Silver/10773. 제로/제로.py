import sys
input = sys.stdin.readline

K= int(input().strip())
A=[]
for _ in range(K):
    num = int(input().strip())
    if num != 0:
        A.append(num)
    else:
        A.pop()
print(sum(A))