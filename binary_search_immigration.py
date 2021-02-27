def compare(n, times, min_time):
    count = 0
    for t in times:
        count += min_time // t
        
    print(count)
    return count < n

def solution(n, times):
    times.sort()   
    left = times[0]
    right = times[0] * n
    while(left + 1 < right):
        mid = (left + right) // 2
        result = compare(n, times, mid)
        print(left, mid, right, result)
        if result:
            left = mid
        else:
            right = mid
            
    return right

print(solution(6, [7, 10]))