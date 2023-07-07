def solution(name, yearning, photo):
    answer = []
    photo_dict = {idx:human for human,idx in enumerate(name)}
    for names in photo:
        count=0
        for id in names:
            idx = photo_dict.get(id)
            if idx is not None:
                count+=yearning[idx]
        answer.append(count)
    return answer
