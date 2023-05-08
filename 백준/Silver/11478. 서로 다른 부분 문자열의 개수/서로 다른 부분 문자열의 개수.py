import sys
input = sys.stdin.readline

# ababc 입력시 -> a,b,a,b,c -> ab,ba,ab,bc -> aba,bab,abc -> abab,babc -> ababc
# 문자열의 모든 가능한 부분 문자열을 구하자 -> 리스트 슬라이싱 활용.
S = input().strip()
A = []

# i=0 -> j=1,2,3,4...len(S), i=1 -> j=2,3,4,....len(S), i=len(S)-1 -> j=len(S)까지
for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        A.append(S[i:j])
print(len(set(A)))