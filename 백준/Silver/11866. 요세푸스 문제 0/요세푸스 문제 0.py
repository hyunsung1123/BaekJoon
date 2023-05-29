import sys
from collections import deque
input = sys.stdin.readline

# 큐 -> FIFO 
# 1 2 3 4 5 6 7
# 입력 7,3 -> 3번째 사람 제거.
# 4,5,6,7,1,2
# 또 3번째 사람제거
# 7,1,2,4,5
# 즉 큐의 길이가 0이 될때 까지 제거가 되는 기준 앞의 원소를 popleft()하고 append()하고 제거되는 원소를 pop하여 list에 저장. 반복
N,K= map(int,input().strip().split())
queue = deque(i for i in range(1,N+1))
result = [] #결과를 담을 리스트
while(len(queue)!=0):
    for i in range(K-1): #제거 될 원소 앞까지 맨뒤로 보내기.
        queue.append(queue.popleft())
    result.append(queue.popleft())
print("<",end='')
print(*result,sep=', ',end='')
print(">")
