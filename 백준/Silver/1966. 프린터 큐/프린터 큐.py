import sys
from collections import deque
input = sys.stdin.readline

# 큐 -> FIFO 
# 큐의 가장 앞에 있는 문서의 중요도 확인.
# 가장 앞의 문서의 중요도 < 나머지 문서의 중요도 -> 맨뒤로 보내기
# 그렇지 않으면 문서 출력.
# EX) 문서 A,B,C,D -> 중요도 2,1,4,3 일때 C먼저 인쇄, D인쇄. A,B 인쇄.
# 1 1 1 3 -> 1 1 3 1 
# 0 1 2 3 -> 1 2 3 0 
N = int(input().strip())
for _ in range(N):
    count = 0
    N,M = map(int,input().strip().split())
    importance = list(map(int,input().strip().split()))
    dict_A = {x:y for x,y in enumerate(importance)}
    queue_A = deque(dict_A.items())
    while(True):
        flag=0
        if len(queue_A) == 0:
            break
        first_element = queue_A.popleft()  # 맨 앞 요소 저장
        rest_elements = list(queue_A)[:][:]  # 나머지 요소 저장
        count +=1
        if any(element[1] > first_element[1] for element in rest_elements):
            count -= 1
            queue_A.append(first_element)
        elif first_element[0] == M:
            break
    print(count)
