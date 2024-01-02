import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
various_count = 0
graph=[[] for i in range(N+1)]
visited = [0]*(N+1)

def dfs(graph,v,visited):
    global various_count
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            various_count +=1
            dfs(graph,i,visited)

for i in range (M):
    start,destination = map(int,input().strip().split())
    graph[start].append(destination)
    graph[destination].append(start)

dfs(graph,1,visited)
print(various_count)