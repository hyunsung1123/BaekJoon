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

#다른사람푼거보니 list slicing 공부 다시해야겠다 느낌
#  start, stop, step 세 개의 숫자를 사용해서 리스트를 다양하게 슬라이싱할 수 있습니다.
# list [ start : stop: step]
# list[::-1] -> 꺼꾸로 슬라이싱됨을 활용!
