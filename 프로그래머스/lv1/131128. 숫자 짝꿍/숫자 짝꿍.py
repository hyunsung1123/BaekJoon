# X,Y를 내림차순으로 정렬한후 큐를 사용해서 왼쪽에서 하나씩 뽑아서 비교한다.
# 같으면 answer에 그값을 더해주고 아니면 두 값을 비교해 작은값은 다시 넣어준다.
# 두개의 큐 중 한개가 다 없어질때까지 비교를 반복.
from collections import deque
def solution(X, Y):
    answer = ''
    x_list = list(X)
    y_list = list(Y)
    x_list.sort(reverse=True)
    y_list.sort(reverse=True)
    x_list=deque(x_list)
    y_list=deque(y_list)
    while(True):
        if x_list:
            x=x_list.popleft()
        else:
            break
        if y_list:
            y=y_list.popleft()
        else:
            break
        if x==y:
            answer+=x
        elif x>y:
            y_list.appendleft(y)
        else:
            x_list.appendleft(x)
    if answer=="":
        answer="-1"
    elif all("0"==i for i in answer):
        answer="0"
    return answer