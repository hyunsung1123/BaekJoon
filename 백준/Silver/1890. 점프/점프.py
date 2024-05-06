import sys

input = sys.stdin.readline

# dfs로 하니 시간초과 뜸..
# def dfs(i, j):
#     global count
#     if i >= N or j >= N:
#         return 0

#     if arr[i][j] == 0:
#         count += 1
#         return 0

#     dfs(i+arr[i][j], j)
#     dfs(i, j+arr[i][j])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# dp[i][j] -> 0,0에서 i,j로 가는 경로의 개수
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        # dp의 값이 0보다 크고 arr값이 0보다 커야 이동할 수 있으므로.
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]
            if i+jump < N:
                dp[i+jump][j] += dp[i][j]
            if j+jump < N:
                dp[i][j+jump] += dp[i][j]
print(dp[N-1][N-1])
