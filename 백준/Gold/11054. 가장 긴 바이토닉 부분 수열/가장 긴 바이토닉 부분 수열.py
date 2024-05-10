# for문 돌면서 현재 수를 기준으로 나올 수 있는 증가하는 수열의 길이, 감소하는 수열의 길이를
# 각각 저장해준다.

N = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]  # 감소하는 수열에 사용할 뒤집은 리스트.
# dp 에 사용될 리스트 선언
increase = [0] * N
decrease = [0] * N
increase[0] = 1
decrease[0] = 1
for i in range(1, N):
    mx = 0
    my = 0
    for j in range(0, i):
        if arr[i] > arr[j]:
            mx = max(mx, increase[j])
        if reverse_arr[i] > reverse_arr[j]:
            my = max(decrease[j], my)
    increase[i] = mx + 1
    decrease[i] = my + 1
#감소하는 부분 구하는 수열 -> 뒤집으면 증가하는 수열과 동일한 효과를 얻을 수 있다.
decrease = decrease[::-1]
mx = 0
#이후 증가하는 부분 + 감소하는 부분의 값이 가장 큰 값을 찾고 -1 을 하면 된다.
for i in range(0, N):
    mx = max(mx, decrease[i] + increase[i])
print(mx-1)