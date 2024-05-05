import sys

input = sys.stdin.readline

N = int(input())
arr = []
dp = [0] * N
for _ in range(N):
    arr.append(int(input()))
dp[0] = arr[0]
if N >= 2:
    dp[1] = arr[1] + dp[0]
    for i in range(2, N):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1], dp[i-1])

print(max(dp))
