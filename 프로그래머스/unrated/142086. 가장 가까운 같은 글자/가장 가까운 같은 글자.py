# 처음 나오는 단어 -> 빈 딕셔너리에 추가
# 이전에 나온 적이 있는 단어 -> 딕셔너리에 key로 접근하여 인덱스 추출 자신이 들어갈 인덱스와 빼준걸 
# answer에 추가 후 해당 key의 인덱스를 새로운 인덱스로 변경.

def solution(s):
    answer = []
    answer_dict = {}
    interval = 0
    for idx,key in enumerate(s):
        if key not in answer_dict:
            answer.append(-1)
            answer_dict[key] = idx
        else:
            index = answer_dict.get(key)
            interval = idx - index
            answer_dict[key] = idx # 딕셔너리 업데이트.
            answer.append(interval) # 간격 answer에 추가.
    return answer