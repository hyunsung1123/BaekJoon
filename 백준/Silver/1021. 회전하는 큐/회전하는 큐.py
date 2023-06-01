import sys
from collections import deque
input = sys.stdin.readline

# 큐 -> FIFO 
# 짝수일때 10일땐 5까지는으로, 6부터 뒤로,
# 홀수일때 9일때 5까지 앞으로, 6부터 뒤로
# queue에 1,2,3,4,5,6,7,8,9까지 존재한다고 하자.
# 내가 찾고하자 하는 search를 2,9,5라고 하면,
# 2는 현재 맨앞에있는 1과 가까이있으므로 1을 기준으로 회전하는게 빠르다.
# 2,3,4,5,6,7,8,9,10,1 -> 맨 앞이 2이므로 popleft() 수행
# 3,4,5,6,7,8,9,10,1 에서 내가 찾고자하는건 9
# 9는 오른쪽으로 세칸 이동시켜야한다.
# 9,10,1,3,4,5,6,7,8 -> 맨 앞 9 이므로 popleft()수행
# 10,1,3,4,5,6,7,8 내가 찾고자하는건 5
# 5가 맨 앞으로 나오기 위해선 오른쪽으로 4번 수행.

N,M = map(int,input().strip().split())
queue = deque(i for i in range(1,N+1))
search = list(map(int,input().strip().split()))
count =0
for i in search:
    while(True):
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i)>len(queue)//2:
                queue.appendleft(queue.pop())
            else:
                queue.append(queue.popleft())
            count+=1
print(count)