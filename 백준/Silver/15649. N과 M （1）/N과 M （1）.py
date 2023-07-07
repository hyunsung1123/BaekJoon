import sys
input = sys.stdin.readline

# 자연수 N,M ->1~N 중에서 길이가 M 인 수열 구하기.

N, M = list(map(int, input().split()))
result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
dfs()
