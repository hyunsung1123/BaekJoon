import sys
input = sys.stdin.readline

def recur_fibo(n):
    global count_recur
    if n==1 or n==2:
        count_recur += 1
        return 1
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
def dp_fibo(n):
    global f, count_dp
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        count_dp += 1
        if f[i] == 0:
            f[i] = f[i-1]+f[i-2]
n = int(input())
count_recur = 0
count_dp = 0
f = [0 for _ in range(n+1)]
recur_fibo(n)
dp_fibo(n)
print(count_recur,count_dp)
