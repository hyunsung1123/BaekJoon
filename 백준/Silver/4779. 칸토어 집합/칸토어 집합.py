import sys
input = sys.stdin.readline

def cantor(array,start,len):
    tmp = len // 3 #각 조각의 길이에 해당. 전체길이 27 -> 9 9 9 로 나눔.
    if tmp == 0:
        return
    cantor(array,start,tmp) #왼쪽
    for i in range(start+tmp, start+tmp*2): #가운데 공백
        array[i] = ' '
    cantor(array,start+tmp*2,tmp) #오른쪽.


while(True):
    try:
        N = int(input())
        array = list("-" for i in range(3**N))
        cantor(array,0,len(array))
        print(''.join(array))
    except:
        break