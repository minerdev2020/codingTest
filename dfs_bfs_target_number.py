def dfs(current : int, numbers : list, result : list, target : int):
    if not numbers:
        if current == target:
            result.append(current)

        return

    dfs(current + numbers[0], numbers[1:], result, target)
    dfs(current - numbers[0], numbers[1:], result, target)

def solution(numbers, target):
    result = []
    dfs(0, numbers, result, target)
    return len(result)

print(solution([1, 1, 1, 1, 1], 3))