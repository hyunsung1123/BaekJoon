answer = [0,0]
def solution(arr):
    global answer
    if all(0 not in row for row in arr): #1만 존재하는지 체크
        answer[1] +=1
    elif all(1 not in row for row in arr): #0만 존재하는지 체크
        answer[0] +=1
    else: #0과 1이 섞여있으므로 arr를 4개로 분할하고 다시 solution을 재귀적으로 호출
        new_len = len(arr)//2
        arr_1 = [row[0:new_len] for row in arr[0:new_len]]
        arr_2 = [row[new_len:len(arr)] for row in arr[0:new_len]]
        arr_3 = [row[0:new_len] for row in arr[new_len:len(arr)]]
        arr_4 = [row[new_len:len(arr)] for row in arr[new_len:len(arr)]]
        solution(arr_1)
        solution(arr_2)
        solution(arr_3)
        solution(arr_4)
    return answer