def compare(rocks, n, min_dist):
    removed = 0
    last = 0
    for i in range(1, len(rocks[1:])):
        gap = rocks[i] - rocks[last]
        if gap < min_dist:
            removed += 1
        else:
            last = i
            
    print(removed)    
    return removed <= n

def solution(distance, rocks, n):
    rocks.insert(0, 0)
    rocks.append(distance)
    rocks.sort()
    left = 0
    right = distance
    while(left + 1 < right):
        mid = (left + right) // 2
        result = compare(rocks, n, mid)
        print(left, mid, right, result)
        if result:           
            left = mid
        else:
            right = mid
            
    return left

print(solution(25, [2, 14, 11, 21, 17], 2))