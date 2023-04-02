import sys
input = sys.stdin.readline
N= int(input())
sum=0
i=0
while True:
    if sum>N:
        break
    i+=1
    sum += i
print(i-1)

