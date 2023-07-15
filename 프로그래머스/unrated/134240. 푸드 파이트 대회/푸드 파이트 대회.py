def solution(food):
    answer = ''
    for index,key in enumerate(food):
        for i in range(int(key//2)):
            answer+=str(index)
    return answer + "0" + answer[::-1]