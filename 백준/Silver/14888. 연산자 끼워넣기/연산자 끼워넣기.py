import sys
input = sys.stdin.readline

maximum = -1e9
minimum = 1e9

def back_tracking (depth,result,plus,minus,mul,div):
    global maximum
    global minimum

    if depth == N:
        maximum = max(result,maximum)
        minimum = min(result,minimum)
        return
    
    if plus > 0:
        back_tracking(depth+1,result+number_list[depth],plus-1,minus,mul,div)
    if minus > 0:
        back_tracking(depth+1,result-number_list[depth],plus,minus-1,mul,div)
    if mul > 0:
        back_tracking(depth+1,result*number_list[depth],plus,minus,mul-1,div)
    if div > 0:
        back_tracking(depth+1,int(result/number_list[depth]),plus,minus,mul,div-1)

N = int(input())
number_list = list(map(int,input().strip().split()))
operator_list = list(map(int,input().strip().split()))

back_tracking(1,number_list[0],operator_list[0],operator_list[1],operator_list[2],operator_list[3])

print(maximum)
print(minimum)