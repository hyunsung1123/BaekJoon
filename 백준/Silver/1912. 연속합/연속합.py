import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int,input().split()))
#dp 리스트 초기화 및 초기값 대입.
dp = [0] * n
dp[0] = num_list[0]
#dp는 최적의 해을 보장함. 
#현재 이전의 dp값에 자기 자신의 수를 더한것과 현재의 수중 큰값을 dp에 저장하면 최적의 해 보장가능.
for i in range(1, n):
    dp[i] = max(num_list[i]+dp[i-1],num_list[i])
print(max(dp))