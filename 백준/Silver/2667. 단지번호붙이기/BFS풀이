import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀 깊이 늘려주기.
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 상하좌우에 1 있는지 검사 -> dfs 재귀반복 .or 범위를 벗어나면 False 반환하도록 .
def bfs(i,j):
    global count
    queue = deque()
    queue.append([i,j])
    graph[i][j] = 0
    count +=1
    while queue:
        x,y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 #방문처리
                queue.append([nx,ny]) #큐에 추가
                count+=1


N = int(input())
graph = [list(map(int,input().strip())) for i in range(N)]

count = 0 # 연결되어있는 집의 개수에 해당.
answer = [] #집의 수를 담아 넣을 리스트에 해당
result = 0 # 만들어지는 단지수
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i,j)
            answer.append(count)
            count = 0
answer.sort()
print(len(answer))
print(*answer)
