def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        check_word=t[i:i+len(p)]
        if int(check_word) <= int(p):
            answer+=1
    return answer