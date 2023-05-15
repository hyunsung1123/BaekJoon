import sys
input = sys.stdin.readline

N= int(input().strip())
A=[]
for _ in range(N):
    command = input().strip()
    if "push" in command:
        a,b=command.split()
        A.append(b)
    elif command == 'top':
        if len(A) == 0:
            print(-1)
        else:
            print(A[-1])
    elif command == 'pop':
        if len(A) == 0:
            print(-1)
        else:
            print(A.pop())
    elif command == 'empty':
        if len(A) == 0:
            print(1)
        else:
            print(0)
    elif command == 'size':
        print(len(A))