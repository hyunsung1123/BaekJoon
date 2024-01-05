import sys

input = sys.stdin.readline
sudoku = []
blank = []
# 스도쿠의 빈칸을 기준으로 가로 세로, 인접 8칸을 다 비교해줘야한다.
#가로 비교 함수
def checkRow(x,n):
    for i in range(9):
        #같은 행에 이미 해당 값이 있는 경우 return False
        if sudoku[x][i] == n:
            return False
    return True
# 세로 비교 함수.
def checkCol(y,n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True
# 3*3 비교 함수
def checkRect(x,y,n):
    for i in range(3):
        for j in range(3):
            if sudoku[x//3 * 3 + i][y//3 * 3 + j] == n:
                return False
    return True

def dfs(idx):
    #탈출조건. idx값이 len(black)와 같아지면 더 이상 빈칸이 없다는 조건에 해당.
    if idx == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit()
    
    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            sudoku[x][y] = i
            dfs(idx+1)
            sudoku[x][y] = 0 # 해당 값을 초기화 해줌. 위의 경우가 답이 아닐 수도 있으므로 다른 경우의 수를 찾기 위해

for i in range(9):
    sudoku.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))

                
dfs(0)