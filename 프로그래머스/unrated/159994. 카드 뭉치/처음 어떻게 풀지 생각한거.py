# 처음에는 card1,card2를 딕셔너리로 변환하고 해당 딕셔너리의 key로 접근하여 인덱스번호를 result에 저장하고 result의 순서가 오름차순이 아니면 잘못된 문장이다라는 로직을 짯다.
# 반례를 찾아보니 ['a','b,'c'] ['d','e'] ['b','c'] 이다 result1에는 1,2가 들어가 알맞은것처럼 보이지만 실제로는 a를 사용하지 않고 b,c로 가기 때문에 이건 잘못된 문장이 답이다..
# 결론 큐를 사용해서 제대로 다시 풀었다.
def solution(cards1, cards2, goal):
    answer = ''
    cards1_dict = {idx:key for key,idx in enumerate(cards1)} #딕셔너리1
    cards2_dict = {idx:key for key,idx in enumerate(cards2)} #딕셔너리2
    flag=True #만들어질수있는지 검사하는 Flag
    result=[] #결과 인덱스를 담을 리스트
    result2=[]
    for word in goal: # 각 idx를 result에 담음
        idx = cards1_dict.get(word)
        if idx is None:
            idx = cards2_dict.get(word)
            result2.append(idx)
        else:
            result.append(idx)
    print(result)
    print(result2)
    for i in range(len(result)-1): # 오름차순으로 되어있는지 검사
        print(i)
        if result[i] > result[i+1]:
            flag=False
            break
    if flag:        
        for i in range(len(result2)-1): # 오름차순으로 되어있는지 검사
            print(i)
            if result2[i] > result2[i+1]:
                flag=False
                break        
    if flag:
        answer="Yes"
    else:
        answer="No"
    return answer
