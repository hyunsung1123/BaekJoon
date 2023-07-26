def solution(numbers):
    answer = 0
    check_num = {i:0 for i in range(10)}
    for idx in numbers:
        check_num[idx] = 1 # numbers에 있는 숫자를 곧 인덱스로 사용해서 해당 인덱스의 값을 1로 변경.
    # 인덱스 값이 0 인 것만 찾아서 해당 키값을 answer에 더해주면 된다.
    for i in check_num:
        if check_num[i] == 0:
            answer+=i
    return answer