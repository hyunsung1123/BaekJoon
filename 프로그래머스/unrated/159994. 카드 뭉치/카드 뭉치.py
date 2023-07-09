from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    flag=True #만들어질수있는지 검사하는 Flag
    
    while goal: #goal에 찾을 값이 남아있을때까지 반복.
        find_item = goal.popleft()
        if cards1:
            cards1_item = cards1.popleft()
        if cards2:
            cards2_item = cards2.popleft()

        if find_item == cards1_item: #card1의 처음원소가 원하는 원소인경우.
            cards2.appendleft(cards2_item) #card2의 원소는 다시 맨앞에 추가.
            
        elif find_item == cards2_item: #card2의 처음원소가 원하는 원소인경우
            cards1.appendleft(cards1_item) #card1의 원소는 다시 맨앞에 추가
            
        else: #맨앞에 있는게 둘다 아닌경우 -> 문장성립X -> flag를 false로 설정 후 break
            flag=False
            break
    if flag:
        answer="Yes"
    else:
        answer="No"
        
    return answer
