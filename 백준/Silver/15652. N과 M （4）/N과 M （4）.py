import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
result = []
check = []
def dfs():
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        if all(i>=j for j in result):
            result.append(i)
            dfs()
            result.pop()
dfs()
