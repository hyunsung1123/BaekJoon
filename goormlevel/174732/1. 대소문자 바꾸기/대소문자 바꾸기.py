import sys
input = sys.stdin.readline

N = int(input())
new_S = [0] * (N+1)
S = input()
for idx,char in enumerate(S):
	if char.isupper():
		new_S[idx] = char.lower()
	else:
		new_S[idx] = char.upper()
print(*new_S,sep='')
