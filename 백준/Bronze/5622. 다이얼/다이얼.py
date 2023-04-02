import sys
input = sys.stdin.readline
sum=0
lst = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'NMO':7,'PQRS':8,'TUV':9,'WXYZ':10}
word = input()
for i in word:
    for key in lst.keys():
        if i in key:
            sum += lst[key]
print(sum)

