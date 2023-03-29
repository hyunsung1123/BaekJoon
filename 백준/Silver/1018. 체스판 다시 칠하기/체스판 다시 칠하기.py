N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

min_cnt = float('inf')
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0 # (i,j)가 W로 시작할 때 칠해야 할 개수
        cnt2 = 0 # (i,j)가 B로 시작할 때 칠해야 할 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0: # 행과 열의 합이 짝수인 경우
                    if board[k][l] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else: # 행과 열의 합이 홀수인 경우
                    if board[k][l] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        min_cnt = min(min_cnt, cnt1, cnt2)

print(min_cnt)