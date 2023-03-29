a =[]
for i in range(5):
    a.append(int(input()))
a.sort()
print(int(sum(a)/5),a[2],sep='\n')