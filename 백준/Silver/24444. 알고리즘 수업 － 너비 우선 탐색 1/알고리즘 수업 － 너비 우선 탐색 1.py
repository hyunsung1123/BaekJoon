import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(graph, v, visited):
  global count
  queue = deque([v])
  visited[v] = count
  #큐가 빈 상태가 될때 까지 반복.
  while queue:
    v = queue.popleft()
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            queue.append(i)
            count +=1
            visited[i] = count
N,M,R = map(int,input().strip().split())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
count = 1
for i in range(M):
    start,destination = map(int,input().strip().split())
    graph[start].append(destination)
    graph[destination].append(start)

bfs(graph,R,visited)

for i in range(1,N+1):
   print(visited[i])