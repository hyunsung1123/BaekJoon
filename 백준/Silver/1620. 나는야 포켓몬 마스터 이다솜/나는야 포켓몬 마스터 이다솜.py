#숫자 -> 포켓몬 이름 출력 OR 포켓몬 이름 입력시 -> 도감에 위치한 key 출력..
import sys
input = sys.stdin.readline

        
n,m= map(int,input().split()) #도감에 수록되어 있는 포갯문 개수 N, 내가 맞춰야할 문제의 개수 M
dict= {}

for i in range(n):
    i=str(i+1)
    dict[i]= input().strip()

di = {v: k for k, v in dict.items()}
a=[]
for i in range(m):
    my_find=input().strip()
    try:
        a.append(dict[my_find])
    except:
        a.append(di[my_find])
print(*a,sep='\n')