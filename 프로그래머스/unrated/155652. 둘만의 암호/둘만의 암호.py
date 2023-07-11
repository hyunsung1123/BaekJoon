# skip에 있는 문자를 포함하지않는 a~z까지의 딕셔너리를 만듬.
# 해당 딕셔너리의 idx를 가져온후 index를 더해서 위의 딕셔너리를 뒤집은 reverse_dict에 key로 사용하여 접근.
def solution(s, skip, index):
    dicts = {}
    count=0
    answer = ''
    for i in range(97,123):
        if chr(i) not in skip: #chr -> 정수를 문자로 변환해줌.
            dicts[chr(i)] = count 
            count+=1
            
    #딕셔너리 key,value값 뒤집기 -> value : key
    reverse_dict = dict(map(reversed,dicts.items()))
    
    for word in s:
        idx = (dicts.get(word) + index) % len(dicts) # idx가 딕셔너리의 최대값을 벗어나는 경우에는 0부터 다시 셀수있도록 나머지 연산수행.
        answer += reverse_dict.get(idx)
    return answer