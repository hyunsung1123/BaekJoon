import sys
input = sys.stdin.readline
# N-QUEEN
# 일차원 배열을 만들어 해당 일차원배열에 값과 다른값을 비교해서 퀸을 놓을수 있는지 없는지 판단
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or x-i == abs(row[x]-row[i]): #x보다 작은 row의 값들을 비교하여 같은 열에 있는지와 대각선에 있는지 검사.
            return False
    return True
    
def dfs(x):
    global result
    if x==N:
        result +=1
        return
    else:
        for i in range(N):
            row[x] = i # x행에 i번째 열에 퀸을 놓겠단 의미.
            if is_promising(x): #row[x]가 허용된다면 x에 1을 증가시켜 dfs 재귀호출.
                dfs(x+1)
N = int(input())
row = [0] * N
result = 0  # 퀸을 놓을 수있는 경우의수를 체크하기위한 변수
dfs(0)
print(result)