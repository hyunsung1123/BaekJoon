import sys
import math
input = sys.stdin.readline
#최빈값 구하기
def most(A):
    B={}
    for val in A:
        try:
            B[val] +=1
        except:
            B[val] = 0
    mx = max(B.values())
    mx_dic = []
    for i in B:
        if mx==B[i]:
            mx_dic.append(i)
    if len(mx_dic) > 1:
        return mx_dic[1]
    else:
        return mx_dic[0]
N = int(input())
A=[]
for _ in range(N):
    A.append(int(input()))
A.sort()
print(round(sum(A)/len(A)))
print(A[math.ceil(len(A)/2)-1])
print(most(A))
print(A[-1]-A[0])