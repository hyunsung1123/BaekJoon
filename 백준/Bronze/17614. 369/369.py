N = int(input())

count = 0

for num in range(1, N+1):
    for i in str(num):
        if int(i) != 0 and int(i) % 3 == 0:
            count += 1

print(count)
