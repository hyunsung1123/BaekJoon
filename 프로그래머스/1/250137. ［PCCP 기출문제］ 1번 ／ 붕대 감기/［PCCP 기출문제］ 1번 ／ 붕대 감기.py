def solution(bandage, health, attacks):
    time = 0
    heal_time = 0
    max_health = health
    i = 0

    while i < len(attacks) and health > 0:
        if attacks[i][0] == time:
            health -= attacks[i][1]
            i += 1
            heal_time = 0
        else:
            heal_time += 1
            if heal_time == bandage[0]:
                health += bandage[2]
                heal_time = 0
            health += bandage[1]

        if health > max_health:
            health = max_health

        time += 1

    if health <= 0:
        return -1

    return health