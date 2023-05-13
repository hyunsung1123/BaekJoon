import sys
input = sys.stdin.readline

N=int(input())
A=[]
sum=0
for _ in range(N):
    chat=input().strip()
    if chat!='ENTER':
        A.append(chat)
    else:
        sum+=len(set(A))
        A=[]
sum+=len(set(A))
print(sum)