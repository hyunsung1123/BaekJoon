def solution(absolutes, signs):
    result = 0
    for idx,key in enumerate(signs):
        if key:
            result += absolutes[idx]
        else:
            result -= absolutes[idx]
    return result