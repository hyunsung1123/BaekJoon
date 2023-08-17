import sys
input = sys.stdin.readline
N = int(input())
A = []
for i in range(0,N):
    a,b = input().split()
    A.append([int(a),b])
A = sorted(A, key=lambda n : n[0])
for i in A:
    print(*i) # 리스트 안에 리스트 형식을 풀어줌