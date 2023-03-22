A = [[0] * 15 for i in range(5)]
str = ""
for i in range(5):
    d = list(input())
    for j in range(len(d)):
        A[i][j] = d[j]
for i in range(15):
    for j in range(5):
        if A[j][i] == 0:
            continue
        else:
            str += A[j][i]
print(str)
