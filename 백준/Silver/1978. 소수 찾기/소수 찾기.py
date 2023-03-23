N = int(input())
M = list(map(int,(input().split(" "))))
count = 0
for i in M:
    if i == 1:
        count -=1
    for j in range(2,i):
        temp = i
        if temp%j == 0:
            count -=1
            break;
    count+=1
if count <0:
    count =0
print(count)

