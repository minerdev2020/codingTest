def solution(clothes):
    hash_table = {}
    for line in clothes:
        if line[1] not in hash_table:
            hash_table[line[1]] = 0
    
    for line in clothes:
        hash_table[line[1]] += 1

    answer = 1
    for value in hash_table.values():
        answer *= value + 1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["red_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["jeans", "pants"]]))