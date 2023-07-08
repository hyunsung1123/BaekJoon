def solution(wallpaper):
    answer = []
    row = len(wallpaper[0])
    high_x,high_y,low_x,low_y=0,0,50,50
    for i in range(len(wallpaper)):
        for j in range(row):
            if wallpaper[i][j] == '#':
                if low_x>i:
                    low_x=i
                if low_y>j:
                    low_y=j
                if i+1>high_x:
                    high_x=i+1
                if j+1>high_y:
                    high_y=j+1
    answer.append(low_x)
    answer.append(low_y)
    answer.append(high_x)
    answer.append(high_y)
    return answer