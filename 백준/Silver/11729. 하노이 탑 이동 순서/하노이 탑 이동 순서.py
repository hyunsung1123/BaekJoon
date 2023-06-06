import sys
input = sys.stdin.readline

#재귀적으로 반복.. 원판의 개수가 1이 되었을때 start -> end로 이동가능.
#총 n개의 원판이 start에 존재한다면 n-1개의 원판을 우선 other로 옮기고.
#나머지 1개의 원판을 start->end로 옮기고 
# n-1개의 원판에 대해 other -> end를 호출하면 된다.
def hanoi(n,start,other,end):
    global result,count
    if n==1:
        count+=1
        result.append((start,end))
        return
    else:
        hanoi(n-1,start,end,other)
        result.append((start, end))
        count+=1
        hanoi(n-1,other,start,end)

N = int(input().strip()) # 원판의 개수.
start=1
destination=3
other=2
count = 0
result=[]
hanoi(N,start,other,destination)
print(count)
for i in result:
    print(*i)