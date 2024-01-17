from collections import deque

def is_one_diff(word1, word2):
    # 두 단어 간의 차이가 한 개의 문자인지 확인하는 함수
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 단계 수)
    visited = set()

    while queue:
        
        current_word, steps = queue.popleft()
        
        #탈출 조건
        if current_word == target:
            return steps

        for next_word in words:
            if next_word not in visited and is_one_diff(current_word, next_word):
                visited.add(next_word)
                queue.append((next_word, steps + 1))

    return 0  # 변환할 수 없는 경우