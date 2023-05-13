a,b,c = map(int,input().split())
day = (c-b)/(a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)

