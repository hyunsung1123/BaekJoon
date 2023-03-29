N = int(input())
A=[]
for i in str(N):
    A.append(i)
A.sort(reverse=True)
print(*A,sep="")