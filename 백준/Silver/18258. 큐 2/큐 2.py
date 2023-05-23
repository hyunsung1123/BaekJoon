import sys
input = sys.stdin.readline

# 큐 -> FIFO
N = int(input())
A = []
front = 0
count = 0 
for _ in range(N):
    command = input().strip()
    if "push" in command:
        a,num = command.split()
        A.append(num)
        count +=1
    elif command == "pop":
        if len(A) == front:
            print(-1)
        else:
            print(A[front])
            front += 1
            count -=1
    elif command == "size":
        print(count)
    elif command == "empty":
        if count == 0:
            print("1")
        else:
            print("0")
    elif command == "front":
        if count == 0:
            print("-1")
        else:
            print(A[front]) 
    elif command == "back":
        if count == 0:
            print("-1")
        else:
            print(A[-1])

        
