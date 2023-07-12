import sys
input = sys.stdin.readline


def check(arr, N):
    global white_cnt, blue_cnt
    # arr에 0이 없는경우. -> 다 1 인경우.
    # any()는 포함된 값 중 어느 하나가 참이라면 항상 참으로 출력한다. 논리 연산의 OR과 비슷하다.
    # 반면 all()이라는 함수는 모든 값이 참이어야 True를 출력한다.
    if all(0 not in l for l in arr):
        # print("all_1",*arr)
        white_cnt += 1
        return True
    # arr에 1이 없는 경우 -> 다 0 인 경우
    elif all(1 not in l for l in arr):
        # print("all_0",*arr)
        blue_cnt += 1
        return True
    # 그렇지 않으면 0,1이 다있으니 분할해서 다시 check 호출.
    else:
        # 전체를 4개로 분할 -> list slicing 사용.
        # 이차원 배열 슬라이싱 하는법 -> For in 으로 한줄 뽑아와서
        # 거기서 슬라이싱해서 새로운 배열에 저장???
        NEW = N//2
        arr_1 = [row[0:NEW] for row in arr[0:NEW]]
        arr_2 = [row[NEW:N] for row in arr[0:NEW]]
        arr_3 = [row[0:NEW] for row in arr[NEW:N]]
        arr_4 = [row[NEW:N] for row in arr[NEW:N]]
        check(arr_1, NEW)
        check(arr_2, NEW)
        check(arr_3, NEW)
        check(arr_4, NEW)


N = int(input())  # 전체 종이의 한변의 길이 N
white_cnt = 0
blue_cnt = 0
# 하얀색은 0 파란색은 1... 빈칸으로 구분하기 위해 split()사용.
arr = [list(map(int, input().split())) for _ in range(N)]
check(arr, N)
print(blue_cnt)
print(white_cnt)
