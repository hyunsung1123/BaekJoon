import sys
input = sys.stdin.readline
A = [i for i in range(1,31)]
for i in range(28):
    A.remove(int(input()))
print(*A, sep='\n')