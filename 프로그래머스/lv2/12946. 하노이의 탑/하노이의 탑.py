
def solution(n):
    answer = []
    def hanoi(n,start,other,destination):
        if n==1: #탈출조건.
            answer.append([start,destination])
            return
        hanoi(n-1,start,destination,other)
        hanoi(1,start,other,destination)
        hanoi(n-1,other,start,destination)
    hanoi(n,1,2,3)
    return answer