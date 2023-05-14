import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
A=dict()
for _ in range(N):
    word=input().strip()
    if len(word)>=M:
        if word not in A:
            A[word]=0
        else:
            A[word]+=1
dict_list = list(A.items())
dict_list.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(dict_list)):
    print(dict_list[i][0])