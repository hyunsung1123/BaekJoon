import sys
def fibo(n):
    if n <1:
        return 0;
    if n == 1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
input = sys.stdin.readline
n = int(input())
print(fibo(n))
