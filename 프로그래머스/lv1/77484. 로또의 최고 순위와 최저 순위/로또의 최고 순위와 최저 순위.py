from collections import deque
def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    lotto_dic = {0 : 6 , 1 : 6 , 2 : 5, 3 : 4, 4 : 3 , 5 : 2, 6 : 1}
    count1 = 0
    count2 = 0
    for number in lottos:
        if number == 0:
            count2 +=1
        else:
            if win_nums.count(number) > 0:
                count1+=1
                count2+=1
    answer.append(lotto_dic[count2])
    answer.append(lotto_dic[count1])
    return answer