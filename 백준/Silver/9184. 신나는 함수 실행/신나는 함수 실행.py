import sys
input = sys.stdin.readline
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if result[a][b][c]:
        return result[a][b][c]    
    if a < b and b < c:
        result[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return result[a][b][c]
    result[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return result[a][b][c]

result = [[[0]*21 for _ in range(21)] for _ in range(21)] #dp저장에 사용될 3차원 배열 
while(1):
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(",a,', ',b,', ',c,") = ",w(a,b,c),sep='')

