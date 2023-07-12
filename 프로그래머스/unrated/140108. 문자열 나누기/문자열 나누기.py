# 문자열 s -> 첫 글자 추출 해야하니 큐 사용??
# pop한 문자 <-> 그 다음 문자 비교 ...
from collections import deque

def split(s):
    s=deque(s)
    result = []
    same_char = 1
    diff_char = 0
    first = s.popleft() 
    answer = first
    if len(s)==0:
        result.append(answer)
    while s:
        if first == s[0]:
            same_char +=1
        else:
            diff_char +=1
        answer += s.popleft()
        if same_char == diff_char:
            result.append(answer)
            same_char,diff_char=1,0
            if s:
                first = s.popleft()
                answer = first
                if len(s)==0:
                    result.append(answer)
                    break
        elif same_char != diff_char and len(s) ==0:
            result.append(answer)
            break
    print(result)
    return len(result)
def solution(s):
    answer = split(s)
    return answer