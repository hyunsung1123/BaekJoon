import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(0, N):
    for j in range(0, M):
        if i == 0:
            if j == 0:
                dp[i][j] = arr[i][j]
            else:
                dp[i][j] = arr[i][j] + dp[i][j-1]
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]

            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j],
                               dp[i][j-1]) + arr[i][j]

print(dp[N-1][M-1])
