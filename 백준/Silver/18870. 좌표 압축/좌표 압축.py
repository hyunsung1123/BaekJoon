import sys
input = sys.stdin.readline

N = int(input())
result = list(map(int, input().split()))
a = sorted(list(set(result)))
a_dict = {val: idx for idx, val in enumerate(a)}
answer = [a_dict[i] for i in result]
print(*answer)
