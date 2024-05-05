# dp배열 만들고 초기 값으로 초기화.
# dp[i][0] -> i번째 집 0번째 색으로 칠할때에 최소 비용을 나타낸다
import sys
input = sys.stdin.readline
N = int(input())
cost_list = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = cost_list[0]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost_list[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost_list[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + cost_list[i][2]

print(min(dp[-1]))