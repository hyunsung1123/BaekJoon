import sys
import math
input = sys.stdin.readline

N = int(input())
A=[]
B=[]
for _ in range(N):
    A.append(int(input().strip()))
A.sort()
for idx,val in enumerate(A): # 가로수 끼리의 거리 저장.
    if idx==N-1:
        break
    else:
        B.append(A[idx+1]-val)
B.sort()
#최대공약수가 1 이면 거리에서 -1 한게 설치해야하는 가로수의 수
#그 외는 거리에서 최대공약수를 나눈 몫의 합
# B의 원소들로 최대공약수구하기
gcd = B[0]
for i in range(1, len(B)):
    gcd = math.gcd(gcd, B[i])
if gcd==1:
    for i in range(len(B)):
        B[i] -=1
else:
    for i in range(len(B)):
        if B[i]==gcd:
            B[i]=0
        else:
            B[i] = (B[i]//gcd) -1
sum=0
for i in B:
    sum +=i
print(sum)

