def solution(k, score):
    answer = []
    result = []
    for jumsu in score:
        if len(result)+1<=k:
            result.append(jumsu)
            result.sort(reverse=True)
            answer.append(result[-1])
            
        else:
            low_score = result.pop()
            
            if low_score < jumsu:
                result.append(jumsu)
            else:
                result.append(low_score)
                
            result.sort(reverse=True)
            answer.append(result[-1])
    return answer