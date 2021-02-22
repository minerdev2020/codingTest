unvisited = []

def dfs(current : list, computers : list):
    global unvisited
    unvisited.remove(current)

    print(current, unvisited)
    for i, value in enumerate(computers[current]):
        if i != current and value and i in unvisited:
            dfs(i, computers)

def solution(n, computers):
    global unvisited
    unvisited = [i for i in range(n)]
    answer = 0
    while(unvisited):
        dfs(unvisited[-1], computers)
        answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))