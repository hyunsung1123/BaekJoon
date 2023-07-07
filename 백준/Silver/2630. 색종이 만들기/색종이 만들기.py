import sys
input = sys.stdin.readline
def check(arr,N):
    global white_cnt, blue_cnt
    # arr에 0이 없는경우. -> 다 1 인경우.
    if all(0 not in l for l in arr):
        #print("all_1",*arr)
        white_cnt +=1
        return True
    # arr에 1이 없는 경우 -> 다 0 인 경우
    elif all(1 not in l for l in arr):
        #print("all_0",*arr)
        blue_cnt +=1
        return True
    # 그렇지 않으면 0,1이 다있으니 분할해서 다시 check 호출.
    else:
        NEW = N//2
        arr_1 = [row[0:NEW] for row in arr[0:NEW]] 
        arr_2 = [row[NEW:N] for row in arr[0:NEW]]
        arr_3 = [row[0:NEW] for row in arr[NEW:N]]
        arr_4 = [row[NEW:N] for row in arr[NEW:N]]
        check(arr_1,NEW)
        check(arr_2,NEW)
        check(arr_3,NEW)
        check(arr_4,NEW)
N = int(input()) # 전체 종이의 한변의 길이 N
white_cnt=0;blue_cnt=0
arr = [list(map(int, input().split())) for _ in range(N)] #하얀색은 0 파란색은 1... 빈칸으로 구분하기 위해 split()사용.
check(arr,N)
print(blue_cnt)
print(white_cnt)
