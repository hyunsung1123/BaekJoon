import sys
input = sys.stdin.readline
N,M = map(int,input().split())
number = list(map(int, input().split()))
result = []
count = 0
def back_tracking(start):
    global count
    # result리스트의 합이 M이랑 같으면 count에 +1 하고 추가적인 재귀호출 반복수행 -> 같은 값이 나올 경우의 수가 존재하므로
    # 즉 다른 가능성이나 경로에 대해 탐색하게된다. return해버리면 재귀를 더 이상 호출하지 않고 마무리.
    if sum(result) == M and len(result) > 0:
        count += 1
    # 백트래킹 수행. result에 처음 원소부터 추가하며 재귀적으로 반복. 
    # 처음 원소를 넣으면 다음 원소를 넣어야하므로 매개변수로 i+1을 받아 반복문의 시작점을 바꿔줌.
    for i in range(start,N):      
        result.append(number[i])
        back_tracking(i+1)
        result.pop()
back_tracking(0)
print(count)

