a = []
b = []
x=0
y=0
for i in range(3):
    x,y= map(int,input().split(" "))
    a.append(x)
    b.append(y)
if a.count(min(a)) == 2:
    x=max(a)
else:
    x=min(a)
if b.count(min(b)) == 2:
    y = max(b)
else:
    y = min(b)
print(x,y)