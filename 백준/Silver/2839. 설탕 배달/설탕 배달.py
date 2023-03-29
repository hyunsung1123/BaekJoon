N = int(input())
count=[]
min_count=0
temp=0
if N%5 == 0:
    count.append(N//5)
if N%3 == 0:
    count.append(N//3)
while True:
    N = N-3
    if N < 0:
        break
    temp +=1
    if N%5 ==0:
        temp = temp + N//5
        count.append(temp)
        break
if len(count)==0:
    count.append(-1)

print(min(count))

# 같은 값에 대한 여러가지의 경우의 수가 나올수있다.
# 90 에 대해서는 3키로 짜리로 30개, 5키로로 18개를 만들수있고
# 그렇기때문에 3키로와 5키로로 둘다 나눠지는 경우 5키로 나누는 경우가 최소값이다.
# 그럼 5키로로 최대한 많이나누고 3키로