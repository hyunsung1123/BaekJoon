# result에 '123'이라는 연속된 문자열이 생기는 순간 해당 문자열을 제외한 부분을 다시 result에 대입.
# answer 에 1을 더해주고 ingredient에 남아있는게 없을때 까지 반복.
from collections import deque
def solution(ingredient):
    result = []
    answer =0
    ingredient = deque(ingredient)
    while ingredient:
        result.append(ingredient.popleft())
        if result[-4::] == [1,2,3,1]:
            for _ in range(4):
                result.pop()
            answer+=1
    return answer