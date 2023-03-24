N = int(input())
A=[]
i = 2
while N >= i:
    if N%i == 0:
        N = N//i
        A.append(i)
        i=2
    else:
        i+=1
for i in A:
    print(i)