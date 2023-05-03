import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split(" ")))
m = int(input())
B = list(map(int, input().split(" ")))
C = [0 for _ in range(len(B))]
a_dict = {val : idx for idx,val in enumerate(B)}
for i in A:
    try:
        if a_dict[i]>=0:
            C[a_dict[i]]=1
    except:
        continue
print(*C)

