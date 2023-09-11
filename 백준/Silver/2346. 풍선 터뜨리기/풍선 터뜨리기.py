import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque(enumerate(map(int,input().split(" "))))
answer = []
while(queue):
    idx, ballon_number = queue.popleft()
    answer.append(idx+1)
    if ballon_number > 0: # 이미 왼쪽으로 한칸씩 떙겨진 상태이므로 1뺀 만큼 회전해줘야한다.
        queue.rotate(-(ballon_number-1))
    else:
        queue.rotate(-ballon_number) #음수인경우 영향을 안받으므로
        
print(*answer)