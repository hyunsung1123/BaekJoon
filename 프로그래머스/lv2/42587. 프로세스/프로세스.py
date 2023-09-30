from collections import deque
def solution(priorities, location):
    answer = 0
    priorities_queue = deque(priorities)
    while priorities_queue:
        max_item = max(priorities_queue)
        now_item = priorities_queue.popleft()
        if location == 0 and now_item >= max_item:
            answer+=1
            break
        if location == 0 and now_item < max_item:
            location = len(priorities_queue)
            priorities_queue.append(now_item)
            continue
        # 현재 해당하는 우선순위보다 높은 우선순위가 있는 경우
        if max_item > now_item:
            priorities_queue.append(now_item)
            location -= 1        
        # 그렇지 않은 경우
        else:
            answer +=1
            location -=1
        
    return answer