from collections import deque

def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)} 
    callings_queue = deque(callings)
    while callings_queue:
        call = callings_queue.popleft()
        index = player_indices.get(call)
        players[index-1], players[index] = players[index], players[index-1]
        player_indices[players[index]] = index
        player_indices[players[index-1]] = index - 1

    return players