# 사과의 상태에 따라 1~k점까지 점수 분류.. 한 상자에 사과를 m개 씩 담아 포장
# 상자의 담긴 사과 중 가장 낮은 점수가 p인 경우 사과 한상자의 가격은 p * m이다.
# 최대 이익을 계산하고자한다. 사과는 상자 단위로 판매. 남는 사과는 버림.
# k=3, m=4 일때 사과의 점수가 1,2,3,1,2,3,1이면 2,3,2,3 으로 구성하여 나온 한개의 사장가 최대 이익이다. 
# -> 1,1,1 남은건 M보다 작으니 버림.
# 이익 발생하지 않는 경우 0 리턴 이익을 리턴해라.
# 방법 -> score을 정렬하고 m만큼 뽑아서 나온 마지막 요소 * k 
def solution(k, m, score):
    answer = 0
    score.sort()
    while score:
        flag=True
        for i in range(m):
            if score:
                a = score.pop()
            else:
                flag=False
                break
        if flag:
            answer += a*m
    return answer