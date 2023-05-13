import sys
input = sys.stdin.readline
N = int(input())
# 초기 점 4개, 1번-9, 2번-25, 3번 81... 
# 한변의 길이가 2^n+1임을 알수있다.
print( (2**N+1)**2)

