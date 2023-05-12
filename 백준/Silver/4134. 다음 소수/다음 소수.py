import sys
import math
input = sys.stdin.readline
#입력받은 수보다 같거나 큰 소수중 작은 수 한개 출력
# 소수를 찾는게 포인트.


def is_prime_number(x):
    if x==1 or x==0:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수 아님
    return True

N = int(input())
A=[]
for _ in range(N):
    n = int(input())
    while(True):
        if is_prime_number(n):
            print(n)
            break
        n+=1
    
