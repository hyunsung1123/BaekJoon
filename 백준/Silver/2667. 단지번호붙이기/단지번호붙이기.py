import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀 깊이 늘려주기.
input = sys.stdin.readline

# 상하좌우에 1 있는지 검사 -> dfs 재귀반복 .or 범위를 벗어나면 False 반환하도록 .
def dfs(i,j):
    global count

    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    
    if graph[i][j] == 1:
        graph[i][j] = 0 # 해당 노드 방문처리
        count += 1 # 연결되어있다는 조건을 만족하므로 count에 +1
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False
N = int(input())
graph = [list(map(int,input().strip())) for i in range(N)]

count = 0 # 연결되어있는 집의 개수에 해당.
answer = [] #집의 수를 담아 넣을 리스트에 해당
result = 0 # 만들어지는 단지수
for i in range(N):
    for j in range(N):
        if dfs(i,j):
            result +=1
            answer.append(count)
            count = 0
answer.sort()
print(result)
print(*answer)