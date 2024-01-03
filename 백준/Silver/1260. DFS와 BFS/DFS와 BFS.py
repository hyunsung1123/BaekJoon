import sys
from collections import deque
sys.setrecursionlimit(10**6) #재귀 깊이 늘려주기.
input = sys.stdin.readline

def dfs(R):
    global order_of_dfs
    DFS_Visited[R] = 1
    order_of_dfs.append(R) #방문한 노드를 저장.
    graph[R].sort() # 그래프의 인접노드를 오름차순으로 정렬
    for i in graph[R]:
        if DFS_Visited[i] == 0:
            dfs(i) # 인접노드에 관해 재귀적으로 dfs 반복수행.

def bfs(R):
    BFS_Visited[R] = 1
    queue = deque([R])
    order_of_bfs.append(R)
    while queue:
        R = queue.popleft()
        for i in graph[R]:
            if BFS_Visited[i] == 0:
                BFS_Visited[i] = 1 #방문처리
                queue.append(i) 
                order_of_bfs.append(i) #방문한 노드를 저장.

N,M,R = map(int,input().strip().split())
graph = [[] for i in range(N+1)]
DFS_Visited = [0] * (N+1)
BFS_Visited = [0] * (N+1)
order_of_dfs = []
order_of_bfs = []
for i in range(M):
    start,destination = map(int,input().strip().split())
    graph[start].append(destination)
    graph[destination].append(start)

dfs(R)
bfs(R)

print(*order_of_dfs)
print(*order_of_bfs)

