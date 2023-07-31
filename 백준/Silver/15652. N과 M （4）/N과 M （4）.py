import sys
input = sys.stdin.readline
N,M = map(int,input().split(" "))
result = []
def dfs(depth,start):
    if depth == M:
        print(*result)
        return
    for i in range(start,N+1):
        result.append(i)
        dfs(depth+1,i)
        result.pop()
dfs(0,1)