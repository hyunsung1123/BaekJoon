import sys
input = sys.stdin.readline
# 4 입력시 [1,2,3,4]가 Push되고 4가 pop되도록.
# 3 입력 [1,2,3] -> 3 POP 되고 [1,2] 리스트 변경
# 6 입력시 -> [1,2,5,6] 으로 추가 되고 6 POP
# 8 입력시 -> []
N = int(input())
A=[]
Result=[]
now = 1
flag=0
for i in range(N):
    number = int(input().strip())
    while (flag==0 and now<=number):
        A.append(now)
        Result.append("+")
        now+=1
    if flag==0 and A[-1] == number:
        A.pop()
        Result.append("-")
    else:
        flag=1
if flag==0:
    print(*Result,sep='\n')
else:
    print("NO")