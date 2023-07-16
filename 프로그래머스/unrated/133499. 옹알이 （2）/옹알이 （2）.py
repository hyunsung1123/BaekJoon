def solution(babbling):
    answer = 0
    for i in babbling:
        my_answer = ["aya","ye","woo",'ma']
        my_str=""
        my_result = []
        flag=True
        for my_char in i:
            my_str+=my_char
            if (my_str in my_answer) and my_str not in my_result:
                my_result=[my_str]
                my_str=""
        if my_str:
            flag=False
        if flag:
            answer+=1
    return answer