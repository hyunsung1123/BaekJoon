N = int(input())
A = []
for i in range(N):
    (x,y)=map(int,input().split(" "))
    A.append((x,y))
A.sort(key = lambda x: (x[1], x[0]))
for i in range(N):
    print(*A[i])