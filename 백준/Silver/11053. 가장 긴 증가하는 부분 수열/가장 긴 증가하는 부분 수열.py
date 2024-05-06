import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

# dp[i] : i번째 숫자 추가시 얻을 수 있는 최대 길이
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    mx = 0
    for j in range(0, i):
        if num_list[i] > num_list[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1
print(max(dp))
