import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,R = map(int,input().strip().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
count = 1

def bfs(graph,V,visited):
    global count
    visited[V] = count
    queue = deque([V])
    while queue:
        item = queue.popleft()
        graph[item].sort(reverse=True)
        for i in graph[item]:
            if visited[i] == 0:
                count +=1
                visited[i]=count
                queue.append(i)
for i in range(M):
    start,destination = map(int,input().strip().split())
    graph[start].append(destination)
    graph[destination].append(start)
bfs(graph,R,visited)
for i in range(1,N+1):
    print(visited[i])