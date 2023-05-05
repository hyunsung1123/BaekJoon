import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
M = int(input())
B = list(map(int, input().strip().split()))

A_dict = {}
for idx, val in enumerate(A):
    if val not in A_dict:
        A_dict[val] = [idx]
    else:
        A_dict[val].append(idx)

answer = []
for val in B:
    if val in A_dict:
        answer.append(str(len(A_dict[val])))
    else:
        answer.append('0')

print(' '.join(answer))
