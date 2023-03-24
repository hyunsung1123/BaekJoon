M = int(input())
N = int(input())
sum= []
result=0
for i in range(M,N+1,1):
    if i!=1:
        sum.append(i)
    for j in range(2,i,1):
        if i%j == 0:
            sum.remove(i)
            break
for i in sum:
    result += i
if len(sum) == 0:
    print(-1)
else:
    print(result)
    print(sum[0])
