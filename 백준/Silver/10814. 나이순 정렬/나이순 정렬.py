import sys
N = int(sys.stdin.readline())
member=[]
for i in range(N):
    age,name=map(str,sys.stdin.readline().split())
    age = int(age)
    member.append((age,name))
member.sort(key = lambda x : x[0])
for i in range(N):
    print(member[i][0],member[i][1])
