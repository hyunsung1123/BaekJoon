import sys
input = sys.stdin.readline
n = int(input())
A = [input().strip().split(" ") for i in range(n)]
A_dict = dict(A)
to_remove = []  # 삭제해야 할 원소의 인덱스를 저장할 리스트
for val in A_dict:
    if A_dict[val] == 'leave':
        to_remove.append(val)
for i in reversed(to_remove):  # 인덱스가 큰 원소부터 삭제해야 함
    del A_dict[i]
keys = list(A_dict.keys())
keys.sort(reverse=True)
for key in keys:
    print(key)
