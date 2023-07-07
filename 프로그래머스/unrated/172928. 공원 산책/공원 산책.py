def solution(park, routes):
    answer = []
    park_list = []
    for i in park:  # 이차원 배열로 바꿈
        park_list.append(list(i))

    x = 0
    for row in park_list:  # 시작 좌표 찾기
        y = 0
        for item in row:
            if item == 'S':
                break
            y += 1
        if item == 'S':
            break
        x += 1

    for route in routes:
        move = True
        direction, square = route.split()
        square = int(square)
        if direction == 'E':
            for i in range(1, square + 1):
                if y + i >= len(park_list[x]) or park_list[x][y + i] == 'X':
                    move = False
                    break
            if move:
                y += square
        elif direction == 'S':
            for i in range(1, square + 1):
                if x + i >= len(park_list) or park_list[x + i][y] == 'X':
                    move = False
                    break
            if move:
                x += square
        elif direction == 'W':
            for i in range(1, square + 1):
                if y - i < 0 or park_list[x][y - i] == 'X':
                    move = False
                    break
            if move:
                y -= square
        elif direction == 'N':
            for i in range(1, square + 1):
                if x - i < 0 or park_list[x - i][y] == 'X':
                    move = False
                    break
            if move:
                x -= square
    answer.append(x)
    answer.append(y)
    return answer