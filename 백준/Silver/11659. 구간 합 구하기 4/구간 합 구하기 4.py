import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_arr = [0]
total = 0
#누적합 리스트 만들기
for i in num_list:
    total += i
    sum_arr.append(total)
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])
