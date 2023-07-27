def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x - i):
            return False
    return True
def n_queens(x):
    global result
    if x == N: #탈출 조건. 놓을 말이 없는 경우
        #print(row)
        result +=1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

N = int(input())
row = [0] * N
result = 0
n_queens(0)
print(result)
