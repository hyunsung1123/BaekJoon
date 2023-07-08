from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    while len(section) !=0:
        start = section.popleft()
        # start+m 처음 칠하는 범위에 section구역이 포함되는 부분까지 pop
        while len(section)!=0 and  start+m > section[0]: 
            section.popleft()
        answer +=1
    return answer