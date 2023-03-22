A = []
str = ""
for i in range(5):
    i = list(input())
    A.append(i)
for i in range(15):
    for j in range(5):
        try:
            str += A[j][i]
        except:
            pass

print(str)
