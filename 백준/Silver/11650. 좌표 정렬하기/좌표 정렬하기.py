N = int(input())
A = []
for i in range(N):
    x = list(map(int, input().split(" ")))
    A.append(x)
A.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(A[i][0],A[i][1])
