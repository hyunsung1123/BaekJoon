import sys
from collections import deque
input = sys.stdin.readline

# 큐 -> FIFO
N = int(input())
queue = deque(i for i in range(1, N+1))
# A의 길이가 1이 될때 까지 반복.
while (len(queue) != 1):
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)

