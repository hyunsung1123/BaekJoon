import sys
from collections import deque
input = sys.stdin.readline

# 큐 -> FIFO 
N = int(input().strip())
queue = deque()
for _ in range(N):
    command = list(input().strip().split())
    if command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif len(queue) == 0:
        print(-1)
    elif command[0] == "pop_front":
        print(queue.popleft())
    elif command[0] == "pop_back":
        print(queue.pop())
    elif command[0] == "front":
        print(queue[0])
    elif command[0] == "back":
        print(queue[-1])
