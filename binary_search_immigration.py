def solution(n, times):
    times.sort()   
    left = times[0]
    right = times[0] * n
    answer = right
    while(left + 1 < right):
        mid = (left + right) // 2
        
        count = 0
        for time in times:
            count += mid // time
        print(left, mid, right, count)
        if n > count:
            left = mid
            
        else:
            right = mid
            if answer > mid:
                answer = mid
            
    return answer

print(solution(6, [7, 10]))