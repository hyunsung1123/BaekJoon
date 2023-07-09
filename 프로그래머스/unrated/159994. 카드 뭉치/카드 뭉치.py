from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    flag=True #만들어질수있는지 검사하는 Flag
    while goal:
        if cards1:
            cards1_item = cards1.popleft()
        find_item = goal.popleft()
        if cards2:
            cards2_item = cards2.popleft()
        print(find_item,cards1_item,cards2_item)
        if find_item == cards1_item:
            cards2.appendleft(cards2_item)
        elif find_item == cards2_item:
            cards1.appendleft(cards1_item)
        else:
            flag=False
            break
    if flag:
        answer="Yes"
    else:
        answer="No"
    return answer