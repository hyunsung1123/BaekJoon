def solution(s):
    answer = ""
    result = ""
    number_to_alpha={"one":"1","two":"2","three":"3", "four":"4","five":"5","six":"6","seven":"7",
    "eight":"8","nine":"9","zero":"0",}
    for i in s:
        # i가 만약 문자라면 result에 그값을 더하고 dic에 result가 존재하면 변환.
        if i.isalpha():
            result += i
        if result in number_to_alpha:
            answer += number_to_alpha[result]
            result=""
        # i가 만약 숫자라면 그냥 바로 answer에 추가.
        if i.isdigit():
            answer += str(i)
    return int(answer)