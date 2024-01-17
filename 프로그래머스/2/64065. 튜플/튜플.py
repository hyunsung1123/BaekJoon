def solution(s):
    answer = []
    dict = {}
    st = ''
    for i in s:
        if i.isdigit():
            st += i
        if st and not i.isdigit():
            if st not in dict:
                dict[st] = 1
                st = ''
            else:
                dict[st] += 1
                st = ''
    a = list(dict.items())
    a.sort(key=lambda x: x[1],reverse=True)
    for key,value in a:
        answer.append(int(key))
    return answer