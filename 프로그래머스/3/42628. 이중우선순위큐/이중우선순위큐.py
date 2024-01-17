import heapq
def solution(operations):
    answer = []
    result = []
    for i in operations:
        oper,num = i.split(" ")
        num = int(num)
        if oper == 'I':
            heapq.heappush(answer,num)
        elif oper =='D' and  num == -1:
            if len(answer):
                heapq.heappop(answer)
        else:
            if len(answer):
                max_value = max(answer)
                answer.remove(max_value)
    if len(answer):
        result =  [max(answer), heapq.heappop(answer)]
    else:
        result = [0,0]
    return result