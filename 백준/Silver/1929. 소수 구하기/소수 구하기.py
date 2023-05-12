import sys
import math
input = sys.stdin.readline
#입력받은 수보다 같거나 큰 소수중 작은 수 한개 출력
# 소수를 찾는게 포인트.

def is_prime_number(x):
    if x==1 or x==0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수 아님
    return True

N,M = map(int,input().strip().split())
A=[]
B=[]
for i in range(1,M+1):
    if is_prime_number(i):
        A.append(i)
for i in range(1,N):
    if is_prime_number(i):
        B.append(i)
C = set(A) & set(B)
D = sorted(list(set(A) - C))
for i in D:
    print(i,end='\n')

    
