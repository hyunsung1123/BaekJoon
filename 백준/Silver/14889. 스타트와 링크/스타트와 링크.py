import sys
input = sys.stdin.readline
N = int(input())
ability = []
for i in range(N):
    ability.append(list(map(int,input().strip().split())))
visited = [0] * N
minimum = 1e9
def back_tracking(depth,idx):
    global minimum
    if depth == N//2:
        team1 = 0
        team2 =0
        for i in range(N):
            for j in range(N):
                if visited[i] == 0 and visited[j] == 0:
                    team1 += ability[i][j]
                elif visited[i] != 0 and visited[j] !=0:
                    team2 += ability[i][j]
        minimum = min(minimum, abs(team1-team2)) #최소값으로 변경

    for i in range(idx,N):
        if visited[i] == 0:
            visited[i] = 1
            back_tracking(depth+1, i+1)
            visited[i] = 0
back_tracking(0,0)
print(minimum)



