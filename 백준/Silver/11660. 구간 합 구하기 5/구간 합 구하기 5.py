import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [[0] * (N+1)]
sum_list = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    num = [0]+list(map(int, input().split()))
    num_list.append(num)
for i in range(1, N+1):
    for j in range(1, N+1):

        sum_list[i][j] = num_list[i][j]
        sum_list[i][j] += sum_list[i][j-1] + sum_list[i-1][j]
        sum_list[i][j] -= sum_list[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_list[x2][y2]
    result -= sum_list[x2][y1-1]
    result -= sum_list[x1-1][y2]
    result += sum_list[x1-1][y1-1]
    print(result)
