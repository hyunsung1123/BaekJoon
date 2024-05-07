import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]


def check(x, y, N):
    now = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if now != arr[i][j]:
                now = -1
                break

    if now == -1:
        print("(", end='')
        N = N // 2
        check(x, y, N)
        check(x, y+N, N)
        check(x+N, y, N)
        check(x+N, y+N, N)
        print(")", end='')

    elif now == 1:
        print(1, end='')
    else:
        print(0, end='')


check(0, 0, N)
