answer=0
def solution(numbers, target):
    global answer
    #숫자 방문처리사용할 리스트
    visited = [False for _ in range(len(numbers))]
    dfs(0,0,target,numbers)
    return answer

def dfs(depth,current,target,numbers):
    global answer
    if depth == len(numbers):
        if current == target:
            answer+=1
            return
    else:
        dfs(depth+1,current+numbers[depth],target,numbers)
        dfs(depth+1,current-numbers[depth],target,numbers)