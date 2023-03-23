# 100 * 100 행렬를만든다.
# 입력된 값에 해당하는 행렬의 사각형 부분의 값을 1로 바꾼다.
# 각 행에 포함된 1의 값을 더해서 출력한다.
num = int(input())
a=[]
sum =0
a = [[0 for j in range(100)] for i in range(100)]
for i in range(num):
    x,y = map(int,input().split(" "))
    for k in range(10):
        for j in range(10):
            a[x+k][y+j]=1
            a[x+j][y+k] =1
for i in range(100):
    sum += a[i].count(1)
print(sum)
