import sys
input = sys.stdin.readline
# 입력한 문자열을 하나씩 list에 저장해줘야한다. 

K= int(input().strip())
for _ in range(K):
    my_str = list(input().strip())
    result = ""
    while(len(my_str) != 0):
        result += my_str.pop(0)
        if "()" in result:
            result = result[:-2]
    if len(result)==0:
        print("YES")
    else:
        print("NO")