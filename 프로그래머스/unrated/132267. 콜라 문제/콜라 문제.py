#n이 a보다 작아지면 나눠지지 않는다. -> 기저조건.
# answer에 n을 a로 나눈몫에 b를 곱하고 n을 남은 병과 마트에서 바꿔온 병의 개수를 더한 새로운 개수로 업데이트
# n이 a보다 작아질때 까지 즉 더이상 바꿀떄 없을때까지 반복.
def solution(a, b, n):
    answer = 0
    while True:
        answer+= (n//a)*b     
        n = n//a*b + n%a
        if n<a:
            break
    return answer