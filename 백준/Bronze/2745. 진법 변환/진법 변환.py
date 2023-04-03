import sys
input = sys.stdin.readline
N,M= input().split(" ")
M = int(M)
N =N[::-1]
sum=0
for i,letter in enumerate(N):
    if letter.isalpha():
        sum = sum + (ord(letter)-55) * (M ** i)
    else:
        sum = sum + int(letter) * (M ** i)
print(sum)