import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀 깊이 늘려주기.
input = sys.stdin.readline

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M: #좌표에 벗어나는 경우 함수 종료
        return
    if graph[x][y] == 1:
        graph[x][y] = 0 #방문처리
        #상하좌우 좌표 재귀수행
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    return

T = int(input())
for i in range(T):
    M,N,K = map(int,input().strip().split())
    result = 0
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        y,x=map(int,input().strip().split()) # x가 가로 y가 세로에 해당하므로 꺼꾸로 받음.
        graph[x][y] = 1 #배추에 좌표에 해당하는 값을 1로 변경
    #세로 0~N-1 각 행 마다 가로 0~M-1의 값 중 1에 해당하는 경우 dfs호출.
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1:
                dfs(j,k)
                result +=1 #dfs가 끝나면 result에1을 더해준다.
    print(result)
