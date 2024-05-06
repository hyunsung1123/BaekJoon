import sys
input = sys.stdin.readline

N = int(input())

# dp[i][j] -> i,j에서 만들수 있는 오르막 수의 개수.
dp = [[0]*10 for _ in range(N)]
dp[0] = [1] * 10

for i in range(1, N):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N-1]) % 10007)
