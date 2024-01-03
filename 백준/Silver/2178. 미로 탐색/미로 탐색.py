import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀 깊이 늘려주기.
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        #현재 좌표에서 상하좌우로 값 비교
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 가로 세로에 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >=M:
                continue
            # 길이 아닌경우 무시
            if graph[nx][ny] == 0:
                continue
            # 길인데 방문한 적이 없는 경우에 해당
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny)) # 큐에 해당 좌표 추가하여 반복 수행

    return graph[N-1][M-1] # 우측하단의 값 반환   
N,M = map(int,input().strip().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().strip())))

print(bfs(0,0))