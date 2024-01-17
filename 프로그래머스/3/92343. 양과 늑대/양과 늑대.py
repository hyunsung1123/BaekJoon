'''
고려해야할 사항
양의 수가 늑대의 수보다 많은가?
부모 노드를 방문한 적이 있는가?
자식 노드를 처음 방문하는가?
'''

def solution(info, edges):
    answer = []
    visited = [False for _ in range(len(info))]
    
    def dfs(sheep, wolf):
        #양의 수가 늑대의 수보다 많으면
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for start,destination in edges:
            if visited[start] and not visited[destination]:
                visited[destination] = True
                if info[destination] == 0:
                    dfs(sheep+1,wolf)
                else:
                    dfs(sheep,wolf+1)
                visited[destination] = False
    visited[0] = True
    dfs(1,0)
    return max(answer)