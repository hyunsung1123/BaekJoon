import sys
imput = sys.stdin.readline

def dfs(depth,idx):
    # result에 크기가 6이 되면 출력하고 함수 반환하여 종료
    if depth == 6:
        print(*result)
        return
    # 각 number_list의 원소를 돌아가면서 result에 넣으면서 재귀적으로 dfs 수행.
    for i in range(idx,number_list[0]+1):
        if not visited[i]:
            visited[i] = True
            result.append(number_list[i])
            dfs(depth+1,i+1)
            visited[i] = False #다른 경우의수도 봐야하므로 visited리스트를 초기화해주고 
            result.pop() #result에 들어있는 원소또한 pop하여 뺴준다.

while True:
    result = []
    number_list = list(map(int,input().strip().split()))
    visited = [False for _ in range(number_list[0]+1)]
    if number_list[0] == 0:
        break
    dfs(0,1)
    print()
    