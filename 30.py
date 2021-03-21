def solution(n, m, height):
    result = 0
    left = 0
    right = 0
    check = False
    for i in height:
        if right < i:
            right = i
    while left <= right:
        mid= (left + right)//2
        tmp_m = 0
        for i in height:
            if (i - mid) > 0:
                tmp_m += (i - mid)
        if tmp_m >= m:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

height = []
n, m = map(int, input().split())
height = list(map(int, input().split()))
result = solution(n, m, height)
print(result)
