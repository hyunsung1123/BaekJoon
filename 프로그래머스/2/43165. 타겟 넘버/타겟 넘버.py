import sys
sys.setrecursionlimit(10**6)
answer=0
def solution(numbers, target):
    global answer
    dfs(0,0,target,numbers)
    return answer

def dfs(depth,current,target,numbers,):
    global answer
    if depth == len(numbers):
        if current == target:
            answer+=1
            return
    else:
        dfs(depth+1,current+numbers[depth],target,numbers)
        dfs(depth+1,current-numbers[depth],target,numbers)
    