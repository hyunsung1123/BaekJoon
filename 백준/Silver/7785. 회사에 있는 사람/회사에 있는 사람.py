import sys
input = sys.stdin.readline

n = int(input())
dict= {}
for _ in range(n):
    name,log = input().strip().split()
    dict[name]=log
    if log == 'leave':
        del dict[name]
dict_key = list(dict.keys())
dict_key.sort(reverse=True)
for i in dict_key:
    print(i)
