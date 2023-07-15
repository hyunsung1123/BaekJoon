def solution(food):
    answer = ''
    temp = []
    for index,key in enumerate(food):
        for i in range(int(key//2)):
            answer+=str(index)
            temp.append(str(index))
    answer+="0"
    while temp:
        answer+=temp.pop()
    return answer