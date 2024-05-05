import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * len(arr[i]) for i in range(N)]
dp[0] = arr[0]

for i in range(1, N):
    for j in range(0, len(dp[i])):
        if j == 0:  # 맨 앞과 맨끝값은 그냥 그대로 내려오기 위함.
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[-1]))
