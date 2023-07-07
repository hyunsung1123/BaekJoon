import sys
input = sys.stdin.readline

# 자연수 N,M ->1~N 중에서 길이가 M 인 수열 구하기.


N, M = list(map(int, input().split()))
result = []
check = []
def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()
dfs()
