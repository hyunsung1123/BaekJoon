def solution(n):
    answer=[]
    triangle = [[0]*n for _ in range(n)] # n*n 이차원 배열생성.
    x,y = -1,0 # 이차원 배열에 접근하기 위한 좌표. 맨처음은 항상 아래로 가닌까 x를 -1로 지정.
    count = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0: #아래로가는경우
                x+=1
            elif i%3 == 1: # 옆으로 가는 경우
                y+=1
            elif i%3 == 2: # 대각선으로 가는 경우
                x-=1
                y-=1
            triangle[x][y] = count 
            count+=1
    for row in triangle:
        for number in row:
            if number!=0: # 0인 값들은 들어가면 안되므로 조건을 건다. 각 행의 값들을 순서대로 넣음.
                answer.append(number)
    return answer
                
            