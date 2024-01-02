import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(graph, v , visited):
    global count
    visited[v] = count 
    graph[v].sort() #오름차순으로 방문을 하므로 정렬해주는 모습
    for i in graph[v]:
        if visited[i] == 0: #인접노드에 방문을 안한 노드가 있다면 방문 처리.
            count+=1 #count를 늘리며 방문순서를 더해주는 모습.
            dfs(graph, i, visited) #해당 노드에서 재귀적으로 dfs처리.
            
count = 1 # 방문순서를 나타낼 글로벌 변수
N,M,R = map(int,input().strip().split()) 
visited = [0] * (N+1) #방문처리에 사용할 리스트
graph = [[] for i in range(N+1)]  #인접 노드에 관한 정보를 담을 리스트
for i in range(M):
    start,destination = map(int,input().strip().split())
    #양방향이므로 두 정점 모두 추가.
    graph[start].append(destination)
    graph[destination].append(start)

dfs(graph,R,visited)
for i in range(1,N+1):
    print(visited[i])