def solution(sizes):
    answer = 0
    max_width,max_height=0,0
    for size in sizes:
        width,height=size[0],size[1]
        if width>max_width:
            max_width=width
        if height>max_height:
            max_height=height
    tmp_width,tmp_height=0,0
    for size in sizes:
        width,height=size[0],size[1]
        if height>width:
            width,height=height,width
        if width>tmp_width:
            tmp_width=width
        if height>tmp_height:
            tmp_height=height
    answer = min(tmp_height,max_height) * max(tmp_width,max_width)
    return answer