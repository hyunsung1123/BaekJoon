# 대충 맞게 짠거같은데 if문을 너무 많이 쓴거같아 보기가 안좋다.
# 좀 줄여보자
def solution(survey, choices):
    answer = ''
    dic = {"RT":0,"TR":0,"CF":0,"FC":0,"JM":0,"MJ":0,"AN":0,"NA":0}
    dic2 = {1:-3,2:-2,3:-1,4:0,5:1,6:2,7:3}
    result = [0 * i for i in range(4)]
    for idx,key in enumerate(survey):
        dic[key] += dic2[choices[idx]]
    for i in dic:
        if i=="RT":
            result[0] += dic[i]
        elif i=="TR":
            result[0] -= dic[i]
        elif i=="CF":
            result[1] += dic[i]
        elif i=="FC":
            result[1] -= dic[i]
        elif i=="JM":
            result[2] += dic[i]
        elif i=="MJ":
            result[2] -= dic[i]
        elif i=="AN":
            result[3] += dic[i]
        elif i=="NA":
            result[3] -= dic[i]
    for idx,key in enumerate(result):
        if idx == 0 and key <=0:
            answer+="R"
        elif idx==0 and key >0:
            answer+="T"
        if idx == 1 and key <=0:
            answer+="C"
        elif idx == 1 and key > 0:
            answer+="F"
        if idx == 2 and key <= 0:
            answer+="J"
        elif idx == 2 and key >0 :
            answer+="M"
        if idx==3 and key <=0:
            answer+='A'
        elif idx == 3 and key >0:
            answer+="N"
    return answer