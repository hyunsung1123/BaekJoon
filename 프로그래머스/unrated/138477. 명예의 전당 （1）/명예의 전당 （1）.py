def solution(k, score):
    answer = []
    result = []
    for jumsu in score:
        result.append(jumsu)
        if len(result)>k:
            result.remove(min(result))
        answer.append(min(result))
    return answer
