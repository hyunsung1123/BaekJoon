def solution(keymap, targets):
    answer = []
    key_dict= {}

    for keys in keymap:
        for index,key in enumerate(keys):
            if key in key_dict:
                if key_dict.get(key) > index+1:
                    key_dict[key]= index+1
            else:
                key_dict[key] = index+1
    for target in targets:
        result=0
        flag = True
        for user_type in target:
            a = key_dict.get(user_type)
            print(a)
            if a is None:
                flag=False
                break
            else:
                result+=a
        print(flag)
        if flag:
            answer.append(result)
        else:
            answer.append(-1)
    return answer

