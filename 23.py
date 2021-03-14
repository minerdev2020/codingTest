def solution(n, s, a, b, fares):

    dist = [[9999 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for pair in fares:
        src, dst, cost = pair
        dist[src-1][dst-1] = cost
        dist[dst-1][src-1] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] + dist[k][j]) < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    s -= 1
    a -= 1
    b -= 1

    answer = dist[s][a] + dist[s][b]

 
    for i in range(n):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
        

    return answer
