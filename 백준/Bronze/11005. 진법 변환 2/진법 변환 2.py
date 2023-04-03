import sys
input = sys.stdin.readline
N,B=map(int,input().split(" "))
A=[]
i=0
while True:
    if N >= B:
        A.insert(0,str(N % B))
        N = N//B
        i+=1
    else:
        i+=1
        A.insert(0,str(N))
        break
for index,letter in enumerate(A):
    if int(letter)>=10:
        a = chr(int(letter)+55)
        if index!=len(A)-1:
            print(a,end='')
        else:
            print(a)
    else:
        if index != len(A)-1:
            print(letter,end='')
        else:
            print(letter)
