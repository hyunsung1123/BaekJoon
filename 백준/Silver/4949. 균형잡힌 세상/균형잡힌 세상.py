import sys
input = sys.stdin.readline
# 입력한 문자열을 하나씩 list에 저장해줘야한다. 

while(True):
    sentence = input().rstrip()
    result = ""
    if sentence == ".":
        break
    sentence_lst = list(sentence)
    while(len(sentence_lst)!=0):
        item = sentence_lst.pop(0)
        if item == "(" or item == ")" or item == "[" or item == "]":
            result += item
        if "()" in result or "[]" in result:
            result = result[:-2]  
    if len(result) == 0:
        print("yes")
    else:
        print("no")