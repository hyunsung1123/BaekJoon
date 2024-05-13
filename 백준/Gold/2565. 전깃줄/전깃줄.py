# 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야하는
# 전깃줄의 최소 개수를 출력해라
# 최소 개수는 = 전체의 갯수 - 엉키지않고 이어질수 잇는 최고길이이므로
# LCS(부분집합중 가장 긴 부분의 길이)로 풀면된다.
# A의 길이로 오름차순 정렬후 B에 대한 최고길이를 구하는 방식으로 품

import sys

input = sys.stdin.readline

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
num_list.sort(key=lambda x: x[0])
dp = [1]*N

for i in range(1, N):
    mx = 0
    for j in range(0, i):
        if num_list[i][1] > num_list[j][1]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1
print(N - max(dp))
