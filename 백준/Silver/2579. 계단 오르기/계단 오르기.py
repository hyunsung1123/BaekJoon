import sys

input = sys.stdin.readline

N = int(input())
stairs = []
dp = [0] * N
for _ in range(N):
    stairs.append(int(input().strip()))
if len(stairs)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + dp[0]
    for i in range(2,N):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
    print(dp[-1])