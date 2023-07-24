# number에서 나올수있는 모든 경우의수 비교 
# ex) number의 개수가 5개라고 할때 1 2 3 4 5 에서 나올수있는 모든 경우의수는
# 1 2 3, 1 2 4, 1 2 5, 1 3 4, 1 3 5, 1 4 5, 2 3 4, 2 3 5, 2 4 5, 3 4 5 
# 5C2 에 해당. 각 경우의수의 합이 0이면 삼총사에 해당하므로 answer 에 1을 더해주는 방법을 구현해보자.
# 조합 라이브러리 쓰면 쉽지만 그냥 직접구현해봄. 
def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k] == 0:
                    answer+=1
    return answer