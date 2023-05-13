import sys
input = sys.stdin.readline


def fact(x):
    if x > 1:
        return x*fact(x-1)
    else:
        return 1

T=int(input())
for _ in range(T):
    A,B=map(int,input().strip().split())
    print(int(fact(B)/(fact(A)*fact(B-A))))

